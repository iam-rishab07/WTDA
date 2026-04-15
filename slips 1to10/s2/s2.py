# Q. 2)Create ‘Salary’ Data set . Build a linear regression model by identifying independent
# and target variable. Split the variables into training and testing sets and print them. Build a simple linear regression model for predicting purchases.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Create the 'Salary' Dataset
data = {
    'YearsExperience': [1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7],
    'Salary': [39343, 46205, 37731, 43525, 39891, 56642, 60150, 54445, 64445, 57189]
}
df = pd.DataFrame(data)

# 2. Independent (X) and Target (y)
X = df[['YearsExperience']] 
y = df['Salary']

# 3. Split into training and testing sets (70:30 ratio)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# 4. Print the sets
print("--- Training Set ---")
print(X_train, "\n", y_train)
print("\n--- Testing Set ---")
print(X_test, "\n", y_test)

# 5. Build and Train the Simple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Print the coefficients and intercept
print("\n--- Model Parameters ---")
print("Coefficients (Slope):", model.coef_) 
print("Intercept:", model.intercept_)

# 7. Example Prediction
pred = model.predict([[5]])
print(f"\nPrediction for 5 years experience: {pred[0]}")