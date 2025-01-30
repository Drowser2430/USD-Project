import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = "Datasets/forestfires_cleaned.csv"
df = pd.read_csv(file_path)

print("✅ Cleaned Dataset Loaded Successfully!\n")

# Display dataset info
print(df.info())

# 🔥 Histogram of Burned Area
plt.figure(figsize=(8,6))
sns.histplot(df["area"], bins=30, kde=True)
plt.title("🔥 Distribution of Burned Area")
plt.xlabel("Burned Area (ha)")
plt.ylabel("Frequency")
plt.show()

# 📊 Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("📊 Feature Correlation Heatmap")
plt.show()

# 🌡️ Scatter Plot: Temperature vs Burned Area
plt.figure(figsize=(8,6))
sns.scatterplot(x=df["temp"], y=df["area"])
plt.title("🌡️ Temperature vs Burned Area")
plt.xlabel("Temperature (Normalized)")
plt.ylabel("Burned Area (ha)")
plt.show()