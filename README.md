# 🌤️ Weather API Fetcher

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)

A simple Python script that connects to the OpenWeatherMap API to fetch real-time weather data for one or more cities entered by the user.

---

## 🔧 What it does

- Prompts the user to input multiple city names (no duplicates)
- Calls OpenWeatherMap API for each city
- Returns key weather info:
  - Temperature
  - Feels like
  - Humidity
  - Sky description
  - Wind speed
- Handles missing or incorrect city names gracefully

---

## 📂 Project structure
weather-api-fetcher/
├── src/
│ └── weather_api_fetcher.py ← main script
├── .gitignore
└── README.md
---

## 🧠 Technologies used

- Python
- requests
- OpenWeatherMap API

---

## 🚀 How to use
1. Clone the repository
2. Replace the API key with your own in the script:
api_key = "your_own_key_here"
3. Run the script:
python src/weather_api_fetcher.py

Počasie pre mesto: Bratislava
- teplota: 24.7
- vlhkosť: 56
- pocitová teplota: 26.1
- obloha: clear sky
- rýchlosť vetra: 2.6

NOTE:
You need a free API key from OpenWeatherMap to run this script.

Tento skript vznikol ako súčasť môjho učenia práce s API v Pythone.
Zadanie obsahovalo získavanie údajov o počasí z verejného API, ich spracovanie a pekný výpis.
Pridanie validácie vstupu a eliminácia duplicít pomohlo zlepšiť používateľský zážitok.
