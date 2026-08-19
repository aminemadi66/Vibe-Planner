🤖 Weekend Activity Planner — AI-Powered Weekend Activity Recommender

«An AI-powered personalized weekend activity recommendation system that combines Machine Learning, real-world OpenStreetMap data, weather conditions, user preferences, budget, and Google Calendar availability to recommend suitable activities for users.»

---

📌 Project Overview

Weekend Activity Planner is an intelligent recommendation system designed to help users find suitable activities for their weekends.

Instead of simply displaying a list of places, the system analyzes multiple factors such as:

- 👤 User preferences
- 📍 User location / city
- 💰 Budget
- 🌦️ Weather conditions
- 🏠 Indoor / outdoor preference
- 👨‍👩‍👧 Family and group suitability
- ♿ Accessibility requirements
- ⭐ Previous user interactions
- 📅 Available time from Google Calendar
- 🏷️ Activity categories
- 📊 Activity quality and historical interaction signals

The Machine Learning model then estimates the probability that a user will prefer an activity and uses that prediction as part of the final recommendation score.

---

👨‍💻 Team

Member| GitHub
Amin| "@YOUR_GITHUB_ID" (https://github.com/YOUR_GITHUB_ID)
Friend 1| "@FRIEND_1_GITHUB_ID" (https://github.com/FRIEND_1_GITHUB_ID)
Friend 2| "@FRIEND_2_GITHUB_ID" (https://github.com/FRIEND_2_GITHUB_ID)
Friend 3| "@FRIEND_3_GITHUB_ID" (https://github.com/FRIEND_3_GITHUB_ID)

«Replace the placeholder GitHub usernames above with the real team members' GitHub IDs.»

---

🎯 Problem

Choosing an activity for the weekend can depend on many different conditions.

For example, a user may want:

- An indoor activity when it is raining.
- An inexpensive activity when their budget is limited.
- A family-friendly activity when traveling with children.
- An accessible location when wheelchair accessibility is required.
- An activity that fits their available free time.
- Something similar to activities they previously liked.

A simple search engine cannot easily combine all of these factors.

Weekend Activity Planner attempts to solve this problem using a personalized Machine Learning recommendation pipeline.

---

💡 Main Idea

The system follows this general pipeline:

User Preferences
       │
       ├── Budget
       ├── City
       ├── Category
       ├── Group Type
       ├── Indoor / Outdoor
       └── Accessibility
       │
       ▼
Activity Dataset
       │
       ▼
Weather Information ───────► Weather Compatibility
       │
       ▼
Google Calendar ───────────► Free Time
       │
       ▼
Feature Engineering
       │
       ▼
XGBoost Recommendation Model
       │
       ▼
Personalized Activity Ranking
       │
       ▼
Top Recommendations

---

🧠 Machine Learning

The recommendation model is based on XGBoost Classification.

The training pipeline combines:

- User information
- Activity information
- Historical interactions
- Ratings
- Interaction types
- Weather context
- Category preferences
- Indoor/outdoor preferences
- Budget compatibility
- Accessibility compatibility
- Group suitability
- Activity quality
- User behavior statistics

The interaction data is converted into a target signal representing whether an activity is likely to be preferred.

Interaction weights

Different interaction types receive different weights:

rating → 1.00
visit  → 0.80
save   → 0.65
view   → 0.25

This allows the model to distinguish between stronger and weaker user signals.

---

📊 Model Performance

The trained XGBoost model was evaluated using a temporal train/test split.

Dataset split

Training samples: 12,869
Testing samples:   2,826
Features:              82

Results

Metric| Score
Accuracy| 91.61%
Precision| 93.23%
Recall| 97.90%
F1 Score| 95.51%
ROC-AUC| 90.50%
PR-AUC| 99.00%

Classification performance

The model achieved particularly strong performance on the positive recommendation class:

Positive-class Precision: 0.93
Positive-class Recall:    0.98
Positive-class F1:        0.96

---

⭐ Important Features

Some of the strongest model features include:

1. "rating_strength"
2. "user_category_positive_rate"
3. "activity_positive_rate"
4. "activity_smoothed_score"
5. "user_indoor_positive"
6. "user_category_rating"
7. "interaction_weight"
8. "behavior_score"
9. "activity_quality"
10. "category_interaction_count"

These features allow the model to learn both user behavior and activity-level patterns.

---

🌎 Dataset

The project contains real-world place data derived from OpenStreetMap.

The dataset contains:

Activities

11,630 named places

across 12 major US cities:

- Boston
- Chicago
- Dallas
- Houston
- Los Angeles
- New York
- Philadelphia
- Phoenix
- San Antonio
- San Diego
- San Francisco
- Seattle

Synthetic Users

1,000 users

The users are completely synthetic and do not represent real people.

Synthetic Interactions

15,695 interactions

The interaction dataset is also synthetic.

---

🏷️ Activity Categories

The dataset contains categories such as:

- 🎢 Amusement
- 🐠 Aquarium
- 📍 Attraction
- 🎬 Cinema
- 🎨 Gallery
- 🌲 Hiking / Nature
- 📚 Library
- 🏛️ Museum
- 🌳 Park
- ⚽ Sports / Fitness
- 🎭 Theatre
- 🦁 Zoo

---

🌦️ Weather Integration

The project contains a dedicated FastAPI service for weather information.

The system can request:

GET /weather/search
GET /weather/forecast
GET /weather/weekend

The most important endpoint for the recommendation system is:

GET /weather/weekend?city=New%20York

This provides weekend weather information and an outdoor suitability score.

The recommendation system can therefore prefer:

Rain
   ↓
Indoor activities

or:

Sunny weather
   ↓
Outdoor activities

---

📅 Google Calendar Integration

The FastAPI service also provides Google Calendar integration.

The system supports:

- OAuth authentication
- Calendar connection status
- Busy periods
- Free-time detection
- Calendar event listing
- Creating activity events
- Deleting events
- Disconnecting the calendar

Main endpoints include:

GET  /calendar/status
GET  /calendar/auth
GET  /calendar/busy
GET  /calendar/free-slots
GET  /calendar/events
POST /calendar/events
DELETE /calendar/events/{event_id}
POST /calendar/disconnect

This makes it possible to move from:

Recommendation
      ↓
User selects activity
      ↓
Find available time
      ↓
Create calendar event

---

🖥️ Web Application

The frontend is implemented using Flask.

Main pages:

/
├── Home
├── About
└── Contact

The Flask application also communicates with the FastAPI service.

Architecture

                 ┌──────────────────────┐
                 │      User / Browser  │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │       Flask App      │
                 │       Port 5000      │
                 └──────────┬───────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
      ┌────────────────┐          ┌────────────────┐
      │ XGBoost Model  │          │    FastAPI     │
      │ weekend_model  │          │    Port 8000   │
      └────────────────┘          └───────┬────────┘
                                          │
                              ┌───────────┴───────────┐
                              ▼                       ▼
                       Weather Service        Google Calendar

The Flask application automatically attempts to start the FastAPI service.

---

📁 Project Structure

Weekend-Activity-Planner/
│
├── README.md
├── README_FA.md
├── requirements.txt
├── app.py
├── weekend_model.pkl
│
├── activities.csv
├── users.csv
├── interactions.csv
├── activity_categories.csv
├── weather_suitability.csv
│
├── data_dictionary.csv
├── feature_importance.csv
├── top10_recommendations.csv
├── validation_report.json
├── weekend_activity_planner_us.sqlite
│
├── weekend_activity_planner.ipynb
│
├── scripts/
│   ├── baseline_recommender.py
│   └── build_weekend_activity_planner_us.py
│
├── raw_overpass/
│   ├── boston.json
│   ├── chicago.json
│   ├── dallas.json
│   ├── houston.json
│   ├── los_angeles.json
│   ├── new_york.json
│   └── ...
│
├── templates/
│   ├── index.html
│   ├── about.html
│   └── contact.html
│
├── Weekend_Activity_Planner_API_Final/
│   ├── README.md
│   ├── TEAM_HANDOFF.md
│   ├── requirements.txt
│   ├── .env.example
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── schemas.py
│   │   └── services/
│   │       ├── weather.py
│   │       ├── google_calendar.py
│   │       └── calendar_slots.py
│   └── tests/
│
└── SOURCES_LICENSE.md

---

⚙️ Technologies

Programming

- Python

Machine Learning

- XGBoost
- Scikit-learn
- Pandas
- NumPy
- Joblib

Backend

- Flask
- FastAPI
- Uvicorn
- Requests

Data

- CSV
- SQLite
- OpenStreetMap
- Overpass API

External Services

- Google Calendar API
- Weather API

Development

- Jupyter Notebook
- Pytest
- Git
- GitHub

---

🚀 Installation

Clone the repository:

git clone https://github.com/YOUR_GITHUB_ID/Weekend-Activity-Planner.git
cd Weekend-Activity-Planner

Install the main dependencies:

pip install -r requirements.txt

---

🌐 FastAPI Setup

Move into the API directory:

cd Weekend_Activity_Planner_API_Final

Create a virtual environment:

python -m venv .venv

Windows

.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env

macOS / Linux

.venv/bin/python -m pip install -r requirements.txt
cp .env.example .env

For Google Calendar integration, add your own credentials to ".env".

GOOGLE_CLIENT_ID=YOUR_CLIENT_ID
GOOGLE_CLIENT_SECRET=YOUR_CLIENT_SECRET
GOOGLE_REDIRECT_URI=http://localhost:8000/calendar/oauth2callback

Never commit the real ".env" file or Google tokens to GitHub.

---

▶️ Running the Application

Return to the project root:

cd ..

Then run:

python app.py

The application starts:

Flask  → http://127.0.0.1:5000
FastAPI → http://127.0.0.1:8000

Open:

http://127.0.0.1:5000

To test the connection between Flask and FastAPI:

http://127.0.0.1:5000/test-api

---

🧪 Running Tests

Inside the FastAPI directory:

python -m pytest -q

---

🔎 Baseline Recommender

A transparent rule-based baseline is included for comparison.

Example:

python scripts/baseline_recommender.py \
    --city Seattle \
    --budget 30 \
    --weather rain \
    --categories museum,gallery

The baseline considers:

- City
- Budget
- Weather
- Activity category
- Indoor/outdoor suitability
- Activity data quality

---

🔐 Security

Sensitive information must never be committed to GitHub.

Do NOT upload:

.env
.secrets/
google_token.json
API keys
Google Client Secrets
Passwords
Access tokens

The repository contains ".env.example" instead of real credentials.

---

⚠️ Data Limitations

OpenStreetMap is community-maintained, so some information may be:

- Missing
- Incomplete
- Outdated
- Incorrect

City assignment is based on collection bounding boxes and does not necessarily represent official municipal boundaries.

Coordinates for OSM ways and relations may represent geometric centers rather than actual entrances.

Estimated prices and durations are heuristic estimates and should not be treated as official venue information.

Users should verify:

- Opening hours
- Prices
- Availability
- Accessibility
- Safety
- Venue information

before making a final plan.

---

📜 Data License & Attribution

The place data is derived from OpenStreetMap through Overpass API and related OSM endpoints.

© OpenStreetMap contributors.

OSM-derived database data is provided under:

Open Data Commons Open Database License (ODbL) 1.0

See:

SOURCES_LICENSE.md

for the complete source and licensing information.

The synthetic users and synthetic interactions were generated by this project and are not real-world user records.

---

🔄 Reproducibility

The project includes scripts for rebuilding and inspecting the dataset:

scripts/build_weekend_activity_planner_us.py
scripts/baseline_recommender.py

The Jupyter Notebook contains the Machine Learning workflow:

weekend_activity_planner.ipynb

The notebook covers:

1. Data loading
2. Data cleaning
3. Feature engineering
4. User/activity merging
5. Target creation
6. Train/test splitting
7. XGBoost training
8. Model evaluation
9. Feature importance
10. Recommendation generation
11. Model export

The trained model is stored as:

weekend_model.pkl

---

📈 Validation

The included validation report confirms:

Activities:          11,630
Cities:                    12
Synthetic users:       1,000
Synthetic interactions: 15,695

Missing names:             0
Missing coordinates:       0
Duplicate OSM IDs:         0
Synthetic flags valid:  TRUE
Cost estimates flagged: TRUE

---

🛣️ Future Improvements

Possible future improvements include:

- Better cold-start recommendations
- More advanced collaborative filtering
- Deep-learning recommendation models
- Real-time venue availability
- More accurate travel-time estimation
- Distance-aware ranking
- Better accessibility information
- More cities and countries
- User feedback loops
- Mobile application
- Deployment to a cloud server
- More detailed weather forecasting
- Automatic calendar-based itinerary generation

---

🏆 Project Goal

The ultimate goal of Weekend Activity Planner is to transform weekend planning from a simple search process into a personalized AI-assisted decision system.

Instead of asking:

«"What can I do this weekend?"»

the user can receive:

«"Based on your preferences, budget, weather, available time, and previous behavior, these are the activities most suitable for you."»

---

👥 Team Collaboration

This project was developed as a collaborative Machine Learning and software engineering project.

Each team member can contribute through GitHub using:

- Commits
- Issues
- Pull Requests
- Code reviews
- Documentation
- Feature development

---

⭐ Conclusion

Weekend Activity Planner combines Machine Learning, real-world geographic data, weather information, calendar availability, and a web interface to provide personalized weekend activity recommendations.

The project demonstrates an end-to-end AI application pipeline:

Real-world Data
      ↓
Data Processing
      ↓
Feature Engineering
      ↓
Machine Learning
      ↓
Recommendation
      ↓
Weather & Calendar Integration
      ↓
Web Application

👨‍💻 Project Creators

This project was designed and developed by:

- Amin Emadi
- Kian Ghassemi Sahebi
- AMIRALI NAJAFLOO
- Mohammadjavad Nouri

---

⭐ Team

Amin Emadi • Kian Ghassemi Sahebi • AMIRALI NAJAFLOO • Mohammadjavad Nouri

«Made with ❤️ by our team.»
