# 🌤️ Weather API Fetcher

A simple Python script that connects to the OpenWeatherMap API to fetch real-time weather data for one or more cities entered by the user.

## 🔧 What it does

- Prompts the user to input multiple city names (no duplicates)
- Calls OpenWeatherMap API for each city
- Returns key weather info:
  - Temperature
  - Feels like
  - Humidity
  - Sky description
  - Wind speed
- Handles missing/incorrect city names gracefully

## 🧠 Technologies used

- Python
- requests
- OpenWeatherMap API

## 🚀 How to use

1. Clone the repository
2. Replace the API key with your own in the script:
```python
api_key = "your_own_key_here"

Example Output
Počasie pre mesto: Bratislava
- teplota: 24.7
- vlhkosť: 56
- pocitová teplota: 26.1
- obloha: clear sky
- rýchlosť vetra: 2.6
