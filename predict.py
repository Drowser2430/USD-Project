import pandas as pd
import joblib

# Load the trained model
model = joblib.load("fire_prediction_model.pkl")

# Function to predict wildfire risk based on temperature, humidity, and wind speed
def predict_fire_risk(temp, humidity, wind_speed):
    input_data = pd.DataFrame([[temp, humidity, wind_speed]], columns=["temp", "RH", "wind"])
    predicted_area = model.predict(input_data)[0]
    print(f"🔥 Predicted Burned Area: {predicted_area:.2f} hectares")

# Example prediction
predict_fire_risk(temp=30, humidity=40, wind_speed=10)