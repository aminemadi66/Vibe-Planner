"""
Flask front-end for the Weekend Activity Planner.

This process serves the static pages (index/about/contact) AND launches +
proxies the separate FastAPI service (Weekend_Activity_Planner_API_Final)
that provides real weather + Google Calendar integration.

Run with:
    python app.py
"""

from __future__ import annotations

import atexit
import shutil
import subprocess
import sys
import time
from pathlib import Path

import joblib
import requests
from flask import Flask, jsonify, render_template, request

# ------------------------------------------------------------------
# Paths (computed relative to THIS file, so the project can live
# anywhere on disk / on any OS / on any machine, no editing required).
# ------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
API_PROJECT = BASE_DIR / "Weekend_Activity_Planner_API_Final"
MODEL_PATH = BASE_DIR / "weekend_model.pkl"

FASTAPI_HOST = "127.0.0.1"
FASTAPI_PORT = 8000
FASTAPI_URL = f"http://{FASTAPI_HOST}:{FASTAPI_PORT}"

# How long to wait for the FastAPI service to come up before giving up
# and starting Flask anyway (it will just report "unreachable" until then).
FASTAPI_STARTUP_TIMEOUT_SECONDS = 20


def _find_api_python() -> str:
    """
    Pick the Python interpreter that should run the FastAPI service.

    Preference order:
      1. The virtualenv inside Weekend_Activity_Planner_API_Final/.venv
         created by setup_windows.bat / setup_mac_linux.sh (this is where
         fastapi/uvicorn/etc. actually get installed per the API's README).
      2. The same interpreter running this Flask app (sys.executable),
         in case the user installed both apps' dependencies into one env.
    """
    venv_dir = API_PROJECT / ".venv"
    candidates = [
        venv_dir / "Scripts" / "python.exe",  # Windows venv
        venv_dir / "bin" / "python",          # macOS / Linux venv
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return sys.executable


def _fastapi_is_up() -> bool:
    try:
        r = requests.get(f"{FASTAPI_URL}/health", timeout=1.5)
        return r.ok
    except requests.exceptions.RequestException:
        return False


def start_fastapi() -> "subprocess.Popen | None":
    """
    Launch the FastAPI service (Weekend_Activity_Planner_API_Final) as a
    child process, using its own virtualenv when available. Returns the
    Popen handle, or None if the API project / its dependencies aren't
    set up yet (Flask still runs; /api/* routes just report the API as
    unreachable until the person runs the API's setup script).
    """
    if not API_PROJECT.exists():
        print(f"[warn] FastAPI project not found at {API_PROJECT}; "
              f"weather/calendar features will be unavailable.")
        return None

    if _fastapi_is_up():
        print(f"[info] FastAPI already running at {FASTAPI_URL}, reusing it.")
        return None

    api_python = _find_api_python()
    print(f"[info] Starting FastAPI with: {api_python}")

    try:
        process = subprocess.Popen(
            [
                api_python,
                "-m",
                "uvicorn",
                "app.main:app",
                "--host",
                FASTAPI_HOST,
                "--port",
                str(FASTAPI_PORT),
            ],
            cwd=str(API_PROJECT),
        )
    except FileNotFoundError:
        print(f"[warn] Could not launch FastAPI: interpreter not found "
              f"({api_python}). Run the API's setup script first "
              f"(setup_windows.bat / setup_mac_linux.sh inside "
              f"{API_PROJECT.name}/).")
        return None

    atexit.register(process.terminate)

    # Wait for it to actually answer /health before handing control back,
    # so the first request Flask forwards doesn't race a cold start.
    deadline = time.monotonic() + FASTAPI_STARTUP_TIMEOUT_SECONDS
    while time.monotonic() < deadline:
        if _fastapi_is_up():
            print(f"[info] FastAPI is up at {FASTAPI_URL}")
            return process
        if process.poll() is not None:
            print("[warn] FastAPI process exited early. Check "
                  f"{API_PROJECT}/requirements.txt is installed "
                  f"(pip install -r requirements.txt) and that a .env "
                  f"file exists (copy .env.example to .env).")
            return None
        time.sleep(0.5)

    print("[warn] FastAPI did not report healthy within "
          f"{FASTAPI_STARTUP_TIMEOUT_SECONDS}s; continuing anyway. "
          "/api/weather will retry the connection on each request.")
    return process


# ------------------------------------------------------------------
# ML model
# ------------------------------------------------------------------
model = None
if MODEL_PATH.exists():
    try:
        model = joblib.load(MODEL_PATH)
    except Exception as exc:  # noqa: BLE001 - surface any load error, don't crash the app
        print(f"[warn] Could not load {MODEL_PATH.name}: {exc}")
else:
    print(f"[warn] Model file not found at {MODEL_PATH}; "
          f"model-backed features will be unavailable.")

# ------------------------------------------------------------------
# Flask app
# ------------------------------------------------------------------
app = Flask(__name__)


# =========================
# صفحات سایت
# =========================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# =========================
# تست اتصال Flask به FastAPI
# =========================

@app.route("/test-api")
def test_api():
    try:
        response = requests.get(f"{FASTAPI_URL}/health", timeout=10)
        return jsonify({
            "status": response.status_code,
            "response": response.json(),
        })
    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": "Cannot connect to FastAPI",
            "details": str(e),
        }), 503


# =========================
# Weather API
# =========================

@app.route("/api/weather")
def get_weather():
    city = request.args.get("city", "New York")

    try:
        response = requests.get(
            f"{FASTAPI_URL}/weather/weekend",
            params={"city": city, "language": "en"},
            timeout=30,
        )

        if not response.ok:
            return jsonify({
                "error": "FastAPI error",
                "status": response.status_code,
                "details": response.text,
            }), response.status_code

        try:
            return jsonify(response.json())
        except ValueError:
            return jsonify({
                "error": "FastAPI did not return JSON",
                "response": response.text,
            }), 502

    except requests.exceptions.Timeout:
        return jsonify({
            "error": "FastAPI request timeout",
            "details": "FastAPI took too long to respond.",
        }), 504

    except requests.exceptions.ConnectionError:
        return jsonify({
            "error": "Cannot connect to FastAPI",
            "details": (
                "Make sure FastAPI is running on port 8000. If you started "
                "Flask with `python app.py` it should have launched "
                "automatically -- check the terminal for a [warn] message."
            ),
        }), 503

    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": "Request failed",
            "details": str(e),
        }), 500


# =========================
# اجرای FastAPI + Flask
# =========================

if __name__ == "__main__":
    print("Starting FastAPI...")
    start_fastapi()

    print("Starting Flask...")
    app.run(host="127.0.0.1", port=5000, debug=False)
