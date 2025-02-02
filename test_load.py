import pandas as pd

# Define the correct path to the dataset
file_path = "Datasets/forestfires.csv"

try:
    # Try to load the dataset
    df = pd.read_csv(file_path)
    print("✅ Dataset loaded successfully!\n")
    print(df.info())  # Print column details
    print("\nFirst 5 Rows:\n", df.head())  # Print first few rows
except FileNotFoundError:
    print("❌ ERROR: File not found! Check the path and try again.")