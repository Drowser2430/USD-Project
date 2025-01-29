import pandas as pd
import matplotlib.pyplot as plt
import warnings

# Function to visualize data
def visualize_data():
    print("Visualization script started...")

    # Step 1: Read data from CSV
    df = pd.read_csv("weather_data.csv")

    # Step 2: Suppress the UserWarning and handle timestamps
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Step 3: Drop invalid timestamps
    df = df.dropna(subset=["timestamp"])

    # Step 4: Remove duplicate rows, keeping the latest for each city
    df = df.sort_values("timestamp").drop_duplicates(subset="city", keep="last")

    # Step 5: Convert temperature from Celsius to Fahrenheit
    df["temperature"] = df["temperature"] * 9/5 + 32

    # Debugging: Print the cleaned data
    print(df)

    # Step 6: Plot Temperature Trends
    plt.figure(figsize=(10, 6))
    for city in df["city"].unique():
        city_data = df[df["city"] == city]
        plt.plot(city_data["timestamp"], city_data["temperature"], label=city)
    plt.title("Temperature Trends")
    plt.xlabel("Timestamp")
    plt.ylabel("Temperature (°F)")
    plt.legend()
    plt.grid()
    plt.show()

    # Step 7: Plot Humidity Trends
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

    # Step 8: Plot Wind Speed Trends
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

# Call the function
if __name__ == "__main__":
    visualize_data()
