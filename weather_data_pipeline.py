import os
import requests
import csv
import time
import datetime

# Define constants
API_KEY = "97b3d69e9de2a926380d626f74808b01" # noqa
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
LOCATIONS = [
    {"city": "Los Angeles", "lat": 34.0522, "lon": -118.2437},
    {"city": "San Bernardino", "lat": 34.1083, "lon": -117.2898},
    {"city": "Malibu", "lat": 34.0259, "lon": -118.7798},
]
OUTPUT_FILE = "weather_data.csv"

# Function to fetch weather data
def fetch_weather_data(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"} 

# Use "imperial" for Fahrenheit
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Function to process and save data
def save_weather_data(data, city):
    # Extract relevant fields
    weather_info = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "wind_direction": data["wind"].get("deg", "N/A"),
        "conditions": data["weather"][0]["description"],
    }

    # Save to CSV
    file_exists = os.path.isfile(OUTPUT_FILE)
    with open(OUTPUT_FILE, "a", newline="") as csvfile:
        fieldnames = weather_info.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()  # Write header only if file doesn't exist
        writer.writerow(weather_info)

# Main loop to fetch data periodically
def main():
    print("Starting data collection...")
    while True:
        for location in LOCATIONS:
            print(f"Fetching weather data for {location['city']}...")
            data = fetch_weather_data(location["lat"], location["lon"])
            if data:
             save_weather_data(data, location["city"])
        print("Data collection cycle complete. Waiting for next cycle...")
        time.sleep(3600)  # Wait for 1 hour

import requests
import csv
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Define constants
API_KEY = "97b3d69e9de2a926380d626f74808b01"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
LOCATIONS = [
    {"city": "Los Angeles", "lat": 34.0522, "lon": -118.2437},
    {"city": "San Bernardino", "lat": 34.1083, "lon": -117.2898},
    {"city": "Malibu", "lat": 34.0259, "lon": -118.7798},
]
OUTPUT_FILE = "weather_data.csv"

# Alert thresholds
WIND_SPEED_THRESHOLD = 20  # in mph
HUMIDITY_THRESHOLD = 15  # in %

# Email settings
SMTP_SERVER = "smtp.gmail.com"  # Replace with your email provider's SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_email_password"  # Replace with your email password
ALERT_RECIPIENT = "recipient_email@example.com"  # Replace with the recipient's email address

# Function to send email alerts
def send_email_alert(city, condition, value):
    subject = f"🔥 Wildfire Risk Alert for {city}!"
    body = f"Critical weather condition detected in {city}:\n{condition}: {value}\nPlease take necessary precautions."
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = ALERT_RECIPIENT

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Alert sent for {city}: {condition} = {value}")
    except Exception as e:
        print(f"Error sending alert: {e}")

# Function to fetch weather data
def fetch_weather_data(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "imperial",  # Use "imperial" for Fahrenheit and mph
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        return None

# Function to process and save data
def save_weather_data(data, city):
    # Extract relevant fields
    weather_info = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "wind_direction": data["wind"].get("deg", "N/A"),
        "conditions": data["weather"][0]["description"],
    }

    # Save to CSV
    file_exists = os.path.isfile(OUTPUT_FILE)
    with open(OUTPUT_FILE, "a", newline="") as csvfile:
        fieldnames = weather_info.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()  # Write header only if file doesn't exist
        writer.writerow(weather_info)

    # Check for alert conditions
    if weather_info["wind_speed"] > WIND_SPEED_THRESHOLD:
        send_email_alert(city, "Wind Speed", weather_info["wind_speed"])
    if weather_info["humidity"] < HUMIDITY_THRESHOLD:
        send_email_alert(city, "Humidity", weather_info["humidity"])

# Main loop to fetch data periodically
def main():
    print("Starting data collection...")
    while True:
        for location in LOCATIONS:
            print(f"Fetching weather data for {location['city']}...")
            data = fetch_weather_data(location["lat"], location["lon"])
            if data:
                save_weather_data(data, location["city"])
        print("Data collection cycle complete. Waiting for next cycle...")
        time.sleep(3600)  # Wait for 1 hour

if __name__ == "__main__":
    main()
WIND_SPEED_THRESHOLD = 0  # Trigger an alert for any wind speed
HUMIDITY_THRESHOLD = 100  # Trigger an alert for any humidity level
import pandas as pd
import matplotlib.pyplot as plt

# Function to visualize data
def visualize_data():
    try:
        # Read data from CSV
        df = pd.read_csv("weather_data.csv")

        # Convert timestamp to datetime for proper plotting
        df["timestamp"] = pd.to_datetime(df["timestamp"])

        # Plot temperature trends
        plt.figure(figsize=(10, 6))
        for city in df["city"].unique():
            city_data = df[df["city"] == city]
            plt.plot(city_data["timestamp"], city_data["temperature"], label=city)
        plt.title("Temperature Trends")
        plt.xlabel("Timestamp")
        plt.ylabel("Temperature (°C)")
        plt.legend()
        plt.grid()
        plt.show()

        # Plot humidity trends
        plt.figure(figsize=(10, 6))
        for city in df["city"].unique():
            city_data = df[df["city"] == city]
            plt.plot(city_data["timestamp"], city_data["humidity"], label=city)
        plt.title("Humidity Trends")
        plt.xlabel("Timestamp")
        plt.ylabel("Humidity (%)")
        plt.legend()
        plt.grid()
        plt.show()

        # Plot wind speed trends
        plt.figure(figsize=(10, 6))
        for city in df["city"].unique():
            city_data = df[df["city"] == city]
            plt.plot(city_data["timestamp"], city_data["wind_speed"], label=city)
        plt.title("Wind Speed Trends")
        plt.xlabel("Timestamp")
        plt.ylabel("Wind Speed (mph)")
        plt.legend()
        plt.grid()
        plt.show()

    except Exception as e:
        print(f"Error visualizing data: {e}")

# Call the visualization function
if __name__ == "__main__":
    visualize_data()
def calculate_risk_score(wind_speed, humidity, temperature):
    wind_factor = 1.5
    humidity_factor = 1.0
    temp_factor = 0.5

    # Calculate the score
    risk_score = (wind_speed * wind_factor) + ((100 - humidity) * humidity_factor) + (temperature * temp_factor)
    return risk_score
df["risk_score"] = df.apply(
    lambda row: calculate_risk_score(row["wind_speed"], row["humidity"], row["temperature"]), axis=1)
