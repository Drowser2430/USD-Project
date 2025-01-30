import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load dataset
file_path = "Datasets/forestfires.csv"
df = pd.read_csv(file_path)

print("✅ Original Data Loaded\n", df.head())

# Convert categorical columns (Month & Day) to numerical
month_mapping = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
df["month"] = df["month"].map(month_mapping)

day_mapping = {'mon': 1, 'tue': 2, 'wed': 3, 'thu': 4, 'fri': 5, 'sat': 6, 'sun': 7}
df["day"] = df["day"].map(day_mapping)

# Normalize temperature, humidity, and wind speed
scaler = MinMaxScaler()
df[["temp", "RH", "wind"]] = scaler.fit_transform(df[["temp", "RH", "wind"]])

# Save cleaned data
df.to_csv("Datasets/forestfires_cleaned.csv", index=False)

print("\n✅ Data Cleaning Complete! Cleaned dataset saved.")
