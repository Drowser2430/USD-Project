import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the cleaned dataset
file_path = "Datasets/forestfires_cleaned.csv"
df = pd.read_csv(file_path)

# Select features (independent variables) and target (dependent variable)
X = df[["temp", "RH", "wind"]]
y = df["area"]

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model using Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f"✅ Model Trained Successfully! Mean Squared Error: {mse:.2f}")

# Save the trained model
import joblib
joblib.dump(model, "fire_prediction_model.pkl")

print("🔥 Model saved as 'fire_prediction_model.pkl'")
