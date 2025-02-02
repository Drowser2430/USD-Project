import pandas as pd
import joblib
import numpy as np

# Load the trained model
model = joblib.load("fire_prediction_model.pkl")

# Function to predict wildfire risk based on temperature, humidity, and wind speed
def predict_fire_risk(temp, humidity, wind_speed, FFMC, DMC, DC, ISI):
    input_data = pd.DataFrame([[temp, humidity, wind_speed, FFMC, DMC, DC, ISI]], 
                              columns=["temp", "RH", "wind", "FFMC", "DMC", "DC", "ISI"])
    log_predicted_area = model.predict(input_data)[0]
    predicted_area = np.expm1(log_predicted_area)
    print(f"🔥 Predicted Burned Area: {predicted_area:.2f} hectares")

# Example prediction
predict_fire_risk(temp=30, humidity=40, wind_speed=10, FFMC=85, DMC=20, DC=500, ISI=6)