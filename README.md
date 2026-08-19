🤖 Weekend Activity Planner

AI-Powered Personalized Weekend Activity Recommendation System

«Weekend Activity Planner is an end-to-end AI recommendation system that helps users discover suitable weekend activities by combining Machine Learning, real-world OpenStreetMap data, weather conditions, user preferences, budget constraints, and Google Calendar availability.»

---

🏆 Project Highlights

- 🤖 XGBoost-based recommendation model
- 📍 11,630 real-world places collected from OpenStreetMap
- 🇺🇸 Coverage across 12 major US cities
- 👤 1,000 synthetic users
- ⭐ 15,695 synthetic interactions
- 🧠 82 engineered features
- 📊 91.61% Accuracy
- 🎯 95.51% F1 Score
- 📈 90.50% ROC-AUC
- 🌦️ Weather-aware recommendations
- 📅 Google Calendar integration
- 🌐 Flask web application
- ⚡ FastAPI backend services
- 🗃️ SQLite database
- 🧪 Automated testing with Pytest
- 📓 Reproducible Jupyter Notebook workflow

---

📌 Project Overview

Choosing an activity for the weekend can depend on many different factors.

A user may want:

- An indoor activity when it is raining.
- An inexpensive activity when their budget is limited.
- A family-friendly activity when traveling with children.
- An accessible activity when accessibility is required.
- An activity that matches their interests.
- An activity that fits their available free time.
- Something similar to activities they previously enjoyed.

Traditional search systems usually treat these requirements independently.

Weekend Activity Planner combines these factors into a personalized recommendation pipeline.

The system analyzes user preferences, activity characteristics, historical interaction signals, weather conditions, and calendar availability to produce relevant activity recommendations.

---

🎯 Problem Statement

The main problem addressed by this project is:

«How can an intelligent system recommend weekend activities that are personalized to a user's preferences, behavior, budget, location, weather conditions, and available time?»

The project approaches this problem as a Machine Learning recommendation task.

Instead of simply returning nearby places, the system attempts to estimate how suitable each activity is for a particular user and then ranks the available activities.

---

💡 Project Goal

The goal of Weekend Activity Planner is to transform weekend planning from a simple search process into an AI-assisted personalized decision system.

Instead of asking:

«"What can I do this weekend?"»

the user can receive recommendations based on:

Who I am
    +
What I like
    +
Where I am
    +
How much I can spend
    +
What the weather is like
    +
When I am free
    ↓
Personalized Recommendations

---

🧠 How the System Works

The complete recommendation pipeline can be summarized as:

                    USER
                     │
                     ▼
            User Preferences
                     │
       ┌─────────────┼─────────────┐
       │             │             │
       ▼             ▼             ▼
    Budget         City       Preferences
       │             │             │
       └─────────────┼─────────────┘
                     ▼
              Activity Dataset
                     │
                     ▼
             Feature Engineering
                     │
       ┌─────────────┼─────────────┐
       │             │             │
       ▼             ▼             ▼
    Behavior      Weather       Calendar
       │             │             │
       └─────────────┼─────────────┘
                     ▼
              XGBoost Model
                     │
                     ▼
            Prediction Scores
                     │
                     ▼
            Activity Ranking
                     │
                     ▼
          Top Personalized Results

---

🔬 Methodology

The project follows an end-to-end Machine Learning workflow.

1. Data Collection

Real-world activity and place information was collected from OpenStreetMap using Overpass API-based data collection.

The resulting dataset contains:

- Place names
- Geographic coordinates
- Activity categories
- Location information
- Indoor/outdoor characteristics
- Accessibility-related information
- Other available OSM attributes

---

2. Data Preparation

The collected data is cleaned and transformed before being used by the recommendation system.

The preparation pipeline includes:

- Data cleaning
- Missing-value handling
- Duplicate checking
- Category normalization
- Feature transformation
- Data validation
- User/activity merging
- Interaction processing

---

3. User and Interaction Data

The project contains synthetic user and interaction data for Machine Learning experimentation.

Users

1,000 synthetic users

The users are artificially generated and do not represent real people.

Interactions

15,695 synthetic interactions

The interaction dataset represents different types of user behavior.

---

⭐ Interaction Modeling

Different interaction types represent different levels of user interest.

The project uses weighted interaction signals:

Interaction| Weight
Rating| 1.00
Visit| 0.80
Save| 0.65
View| 0.25

This allows the recommendation model to distinguish stronger signals from weaker signals.

For example:

Rating
  ↓
Strong preference signal

Visit
  ↓
Strong behavioral signal

Save
  ↓
Medium preference signal

View
  ↓
Weak interest signal

---

🧠 Machine Learning Model

The main recommendation model is based on XGBoost Classification.

The model combines multiple groups of features.

User Features

- User preferences
- User category behavior
- User indoor/outdoor preferences
- User historical ratings
- User positive interaction rates

Activity Features

- Activity category
- Activity quality
- Activity characteristics
- Activity popularity
- Activity interaction statistics

Interaction Features

- Interaction type
- Interaction weight
- Historical behavior
- Rating strength
- Category interaction count

Context Features

- Weather conditions
- Budget compatibility
- Indoor/outdoor suitability
- Accessibility
- Group suitability

The model predicts the probability that a user will positively interact with an activity.

The predicted probabilities are then used to rank candidate activities.

---

🧩 Feature Engineering

The project uses engineered features to capture both user-level and activity-level behavior.

Important features include:

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

These features help the model learn patterns such as:

User preference
      +
Category preference
      +
Activity quality
      +
Historical behavior
      +
Context
      ↓
Recommendation probability

---

📊 Model Evaluation

The model was evaluated using a temporal train/test split to reduce the risk of using future interactions to predict past behavior.

Dataset Split

Item| Value
Training Samples| 12,869
Testing Samples| 2,826
Features| 82

---

🏆 Model Performance

The trained XGBoost model achieved the following results:

Metric| Score
Accuracy| 91.61%
Precision| 93.23%
Recall| 97.90%
F1 Score| 95.51%
ROC-AUC| 90.50%
PR-AUC| 99.00%

Positive-Class Performance

Metric| Score
Precision| 0.93
Recall| 0.98
F1 Score| 0.96

These results indicate that the model is particularly effective at identifying activities that are likely to be positively preferred within the evaluated dataset.

«Important: These metrics are based on the project's available dataset and evaluation setup. They should not be interpreted as a guarantee of real-world recommendation accuracy.»

---

🌎 Dataset

The activity dataset contains real-world geographic information derived from OpenStreetMap.

📍 Activity Coverage

The project contains:

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

---

🏷️ Activity Categories

The dataset contains activity categories including:

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

🌦️ Weather-Aware Recommendations

Weather conditions can significantly affect whether an activity is suitable.

The project includes a dedicated FastAPI weather service.

Available endpoints include:

GET /weather/search
GET /weather/forecast
GET /weather/weekend

Example:

GET /weather/weekend?city=New%20York

The service provides weekend weather information and outdoor suitability information.

The recommendation logic can therefore adapt to conditions such as:

Rainy Weather
     ↓
Prefer Indoor Activities

and:

Good Weather
     ↓
Prefer Outdoor Activities

This creates a more context-aware recommendation system.

---

📅 Google Calendar Integration

Weekend Activity Planner also includes Google Calendar integration.

The purpose is to connect recommendations with the user's available time.

Supported functionality includes:

- OAuth authentication
- Calendar connection status
- Busy period detection
- Free-time detection
- Calendar event listing
- Creating calendar events
- Deleting events
- Disconnecting the calendar

Main Endpoints

GET    /calendar/status
GET    /calendar/auth
GET    /calendar/busy
GET    /calendar/free-slots
GET    /calendar/events
POST   /calendar/events
DELETE /calendar/events/{event_id}
POST   /calendar/disconnect

Example Workflow

Recommendation
      ↓
User selects activity
      ↓
Check calendar
      ↓
Find available time
      ↓
Create calendar event

This allows the recommendation system to move from finding an activity to helping the user schedule it.

---

🌐 Web Application

The project uses Flask for the main web application.

Main Pages

/
├── Home
├── About
└── Contact

The Flask application communicates with the FastAPI services and the Machine Learning model.

---

🏗️ System Architecture

                         ┌─────────────────────┐
                         │       User          │
                         │     / Browser       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Flask App      │
                         │      Port 5000      │
                         └──────────┬──────────┘
                                    │
                  ┌─────────────────┼─────────────────┐
                  │                 │                 │
                  ▼                 ▼                 ▼
          ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
          │ XGBoost      │  │   FastAPI    │  │    SQLite    │
          │ Model        │  │   Port 8000  │  │   Database   │
          └──────────────┘  └───────┬──────┘  └──────────────┘
                                    │
                          ┌─────────┴─────────┐
                          │                   │
                          ▼                   ▼
                  ┌──────────────┐    ┌──────────────┐
                  │   Weather    │    │    Google    │
                  │   Service    │    │   Calendar   │
                  └──────────────┘    └──────────────┘

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

Development & Testing

- Jupyter Notebook
- Pytest
- Git
- GitHub

---

🚀 Installation

1. Clone the Repository

git clone https://github.com/aminemadi66/Weekend-Activity-Planner.git
cd Weekend-Activity-Planner

2. Install Dependencies

pip install -r requirements.txt

---

🌐 FastAPI Setup

Move to the API directory:

cd Weekend_Activity_Planner_API_Final

Create a virtual environment:

python -m venv .venv

Windows

.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env

macOS / Linux

.venv/bin/python -m pip install -r requirements.txt
cp .env.example .env

---

🔐 Environment Variables

For Google Calendar integration, configure your own credentials inside ".env".

Example:

GOOGLE_CLIENT_ID=YOUR_CLIENT_ID
GOOGLE_CLIENT_SECRET=YOUR_CLIENT_SECRET
GOOGLE_REDIRECT_URI=http://localhost:8000/calendar/oauth2callback

Security Rule

Never commit real credentials to GitHub.

Do not upload:

.env
.secrets/
google_token.json
API keys
Client secrets
Access tokens
Passwords

Only the example configuration should be included:

.env.example

---

▶️ Running the Application

Return to the project root:

cd ..

Start the application:

python app.py

The application uses:

Flask   → http://127.0.0.1:5000
FastAPI → http://127.0.0.1:8000

Open the main application at:

http://127.0.0.1:5000

---

🧪 Testing

The FastAPI project includes automated tests.

Run:

python -m pytest -q

Testing is used to help verify that the backend services behave as expected.

---

🔎 Baseline Recommendation System

A rule-based baseline recommender is included to provide a transparent comparison against the Machine Learning approach.

Example:

python scripts/baseline_recommender.py \
    --city Seattle \
    --budget 30 \
    --weather rain \
    --categories museum,gallery

The baseline considers factors such as:

- City
- Budget
- Weather
- Activity category
- Indoor/outdoor suitability
- Activity quality

This provides a simple non-ML reference point for comparison.

---

📓 Reproducibility

The project includes a Jupyter Notebook:

weekend_activity_planner.ipynb

The notebook documents the Machine Learning workflow, including:

1. Data loading
2. Data cleaning
3. Exploratory analysis
4. Feature engineering
5. User/activity merging
6. Target creation
7. Temporal train/test splitting
8. XGBoost training
9. Model evaluation
10. Feature importance analysis
11. Recommendation generation
12. Model export

The trained model is stored as:

weekend_model.pkl

---

📊 Validation

The project includes a validation report:

validation_report.json

Key dataset validation information includes:

Activities:             11,630
Cities:                      12
Synthetic Users:          1,000
Synthetic Interactions:  15,695

The dataset validation process checks important properties such as:

- Missing activity names
- Missing coordinates
- Duplicate OSM identifiers
- Synthetic data flags
- Cost-estimate flags
- Dataset consistency

---

📸 Screenshots & Demonstration

Screenshots of the application can be placed in:

screenshots/

Recommended screenshots for the final project presentation:

1. Main application interface
2. Activity recommendation results
3. Weather-aware recommendation
4. Calendar integration
5. Project architecture
6. Model evaluation results

Example README usage:

## 📸 Screenshots

### Main Interface

![Main Interface](screenshots/main.png)

### Recommendation Results

![Recommendation Results](screenshots/recommendations.png)

---

⚠️ Limitations

Although the project demonstrates an end-to-end personalized recommendation pipeline, there are several limitations.

Synthetic User Data

The user and interaction datasets are synthetic.

Therefore, the model's evaluation results should not be interpreted as real-world user behavior performance.

OpenStreetMap Data

OpenStreetMap is community-maintained.

Some information may be:

- Missing
- Incomplete
- Outdated
- Incorrect

Activity Information

Opening hours, prices, accessibility information, and venue availability may change over time.

Users should verify important information before making a final decision.

Cold Start

New users with little or no interaction history may receive less personalized recommendations.

Geographic Coverage

The current dataset focuses on 12 US cities.

The system can be extended to additional locations.

Weather Dependency

Weather recommendations depend on the availability and accuracy of the external weather service.

External API Dependencies

Google Calendar and weather integration require external services and valid credentials.

---

🔮 Future Improvements

Future versions could include:

- Advanced collaborative filtering
- Neural recommendation models
- Deep learning ranking models
- Real-time venue availability
- Better travel-time estimation
- Distance-aware recommendation ranking
- More accurate accessibility information
- Additional cities and countries
- Real user feedback loops
- Mobile application
- Cloud deployment
- Improved cold-start recommendations
- More advanced weather forecasting
- Automatic multi-day itinerary generation
- Explainable AI recommendations
- Personalized recommendation explanations

---

🔒 Privacy & Security

The project is designed to avoid storing real user credentials inside the repository.

Sensitive configuration values must be stored locally using environment variables.

Real Google Calendar credentials, API keys, passwords, and access tokens must never be committed to the repository.

Synthetic user data is used for the demonstration and Machine Learning workflow.

---

📜 Data Sources & Licensing

The activity dataset is derived from OpenStreetMap data collected through Overpass API and related OSM endpoints.

© OpenStreetMap contributors.

OpenStreetMap data is available under the:

Open Data Commons Open Database License (ODbL) 1.0

Additional source and licensing information is available in:

SOURCES_LICENSE.md

The synthetic users and synthetic interactions were generated for this project and do not represent real-world user records.

---

📦 Important Repository Files

File| Purpose
"app.py"| Main Flask application
"weekend_model.pkl"| Trained XGBoost model
"requirements.txt"| Main Python dependencies
"activities.csv"| Activity/place dataset
"users.csv"| Synthetic user dataset
"interactions.csv"| Synthetic interaction dataset
"weather_suitability.csv"| Weather suitability information
"feature_importance.csv"| Model feature importance
"validation_report.json"| Dataset validation report
"weekend_activity_planner_us.sqlite"| SQLite database
"weekend_activity_planner.ipynb"| ML workflow and experiments
"SOURCES_LICENSE.md"| Data sources and licensing

---

🧪 Quality & Development Practices

The project follows several software and Machine Learning development practices:

- Clear project structure
- Requirements management
- Data validation
- Feature engineering
- Model evaluation
- Temporal train/test splitting
- Automated testing
- Environment-variable based secrets
- Documentation
- Source attribution
- Git version control
- Reproducible experimentation

---

📝 Git Commit Strategy

The repository should use clear and meaningful commits.

Examples:

Initial project upload
Add machine learning pipeline
Improve recommendation model
Add weather integration
Add Google Calendar integration
Add Flask interface
Add automated tests
Add project documentation
Update README
Prepare final release

This makes the development history easier to understand and demonstrates the evolution of the project.

---

🏷️ Final Release

The recommended final release version is:

v1.0.0

The final release should contain:

- Final source code
- Final README
- Requirements
- Model
- Documentation
- Validation results
- Final screenshots
- Final project archive

---

👨‍💻 Project Creators

This project was designed and developed by:

- Amin Emadi — "@aminemadi66"
- Kian Ghassemi Sahebi — "@Kianghassemisahebi-wq"
- AMIRALI — "@rahahoseini2024-bit"
- Mohammadjavad Nouri — "@mjteb21-beep"

---

⭐ Team

Amin Emadi • Kian Ghassemi Sahebi • AMIRALI • Mohammadjavad Nouri

«Made with ❤️ by our team.»

---

🎯 Final Goal

Weekend Activity Planner demonstrates how multiple technologies can be combined into one practical AI application:

Real-World Data
      ↓
Data Processing
      ↓
Feature Engineering
      ↓
Machine Learning
      ↓
Personalized Recommendation
      ↓
Weather Context
      ↓
Calendar Availability
      ↓
Web Application
      ↓
Better Weekend Planning

The project aims to demonstrate not only a trained Machine Learning model, but a complete end-to-end AI product combining data, modeling, backend services, external APIs, user interaction, testing, and documentation.

---

🚀 Built for Innovation

Weekend Activity Planner

«Plan smarter. Discover better. Enjoy your weekend.»
