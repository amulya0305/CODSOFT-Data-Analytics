import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("customers.csv")
print("First 5 Customers:")
print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nDescriptive Statistics:")
print(df.describe())
print("\nAverage Purchase Amount by Location:")
print(df.groupby("Location")["PurchaseAmount"].mean())
df["CustomerSegment"] = pd.cut(
    df["PurchaseAmount"],
    bins=[0, 2000, 4000, 8000],
    labels=["Low Value", "Medium Value", "High Value"]
)
print("\nCustomer Segments:")
print(df["CustomerSegment"].value_counts())
plt.figure(figsize=(8, 5))
sns.barplot(x="Location", y="PurchaseAmount", data=df)
plt.title("Purchase Amount by Location")
plt.xlabel("Location")
plt.ylabel("Purchase Amount")
plt.show()
plt.figure(figsize=(8, 5))
sns.countplot(x="CustomerSegment", data=df)
plt.title("Customer Segments")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.show()
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Age", y="PurchaseAmount", data=df)
plt.title("Age vs Purchase Amount")
plt.xlabel("Age")
plt.ylabel("Purchase Amount")
plt.show()