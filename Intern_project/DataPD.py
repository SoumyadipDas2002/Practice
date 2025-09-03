import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("house_rent_data.csv")
print("First 5 rows:\n", df.head())

avg_rent = df['Rent'].mean()
avg_size = df['Size'].mean()
avg_bedrooms = df['Bedroom'].mean()

print("\nBasic Statistics:")
print(f"Average Rent: ₹{avg_rent:.2f}")
print(f"Average House Size: {avg_size:.2f} sqft")
print(f"Average Number of Bedrooms: {avg_bedrooms:.2f}")

plt.figure(figsize=(8,6))
df.groupby("Location")['Rent'].mean().sort_values().plot(kind="bar", color="skyblue")
plt.title("Average Rent by Location")
plt.ylabel("Average Rent (₹)")
plt.xlabel("Location")
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df["Size"], df["Rent"], alpha=0.6, c="blue")
plt.title("House Size vs Rent")
plt.xlabel("Size (sqft)")
plt.ylabel("Rent (₹)")
plt.show()

le = LabelEncoder()
df["LocationIndex"] = le.fit_transform(df["Location"])

numeric_df = df[["Size", "Beroom", "Rent", "LocationIndex"]]
corr = numeric_df.corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Features")
plt.show()

