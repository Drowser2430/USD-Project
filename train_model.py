import pandas as pd
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 🔥 Load the cleaned dataset
df = pd.read_csv("Datasets/forestfires_cleaned.csv")

# 🔍 Debugging - Print first few rows
print("✅ Checking dataset sample:")
print(df.head())

# 🎯 Select Features & Target Variable (Include Fire Spread Indicators)
X = df[["temp", "RH", "wind", "FFMC", "DMC", "DC", "ISI"]]  # ADD IMPORTANT FIRE FEATURES
y = np.log1p(df["area"]) 

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Better Model: Random Forest Regressor 
print("🔥 Training the Random Forest model...")
model = RandomForestRegressor(n_estimators=500, max_depth=10, min_samples_split=5, min_samples_leaf=2, random_state=42) # MORE TREES & LIMITED DEPTH
model.fit(X_train, y_train)

# 🧪 Test Model & Calculate MSE
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"📉 Model Trained Successfully! Mean Squared Error: {mse:.2f}")

# 💾 Save Model
joblib.dump(model, "fire_prediction_model.pkl")
print("✅ Model saved as 'fire_prediction_model.pkl'")