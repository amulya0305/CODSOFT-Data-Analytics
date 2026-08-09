import pandas as pd

# Load dataset
df = pd.read_csv("titanic.csv")

print(df.head())

print(df.info())

print(df.isnull().sum())

df = df.drop_duplicates()

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df = df.drop(columns=["Cabin"])

df.to_csv("cleaned_titanic.csv", index=False)

print("Data cleaning completed successfully!")
