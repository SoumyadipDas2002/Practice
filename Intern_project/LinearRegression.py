import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score

# Load Dataset 

df = pd.read_csv("house_rent_data.csv")

print("First 5 rows of dataset:\n", df.head())

# Preprocessing

# Encode location into numeric values
le = LabelEncoder()
df["LocationIndex"] = le.fit_transform(df["Location"])

# Define features (independent variables) and target (dependent variable)
X = df[['Size', 'Bedroom', 'LocationIndex']]
y = df['Rent']

# Split Dataset

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression Model

model = LinearRegression()
model.fit(X_train, y_train)
print("\n✅ Model Trained Successfully!")


# Make Predictions

y_pred = model.predict(X_test)

# R² Score (accuracy metric for regression)
print("R² Score of the model: ", r2_score(y_test, y_pred))


# Compare Actual vs Predicted

compare = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred.astype(int)})
print("\nComparison (Actual vs Predicted):\n", compare.head())


# Visualization

plt.scatter(y_test, y_pred, color='red')
plt.xlabel("Actual Rent")
plt.ylabel("Predicted Rent")
plt.title("Actual vs Predicted Rent")
plt.show()


# Test with New Input

new_location = 'Mumbai'
new_location_index = le.transform([new_location])[0]

# Example new house: 1200 sqft, 3 bedrooms, Mumbai
new_data = [[1200, 3, new_location_index]]
predicted_rent = model.predict(new_data)

print(f"\nPredicted rent for {new_data[0][0]} sqft, {new_data[0][1]} BHK in {new_location} = ₹{predicted_rent[0]:.2f}")
