import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_titanic.csv")

# Display first 5 rows
print(df.head())

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Dataset information
print("\nDataset Information:")
print(df.info())