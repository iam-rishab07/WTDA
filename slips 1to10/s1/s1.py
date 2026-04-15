# Q. 2)Create ‘Position_Salaries’ Data set. Build a linear regression model by identifying
# independent and
# Target variable. Split the variables into training and testing sets. Then divide the training
# and testing sets
# Into a 7:3 ratio, respectively and print them. Build a simple linear regression
# model.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Create the 'Position_Salaries' Dataset
data = {
    'Position': ['Business Analyst', 'Junior Consultant', 'Senior Consultant', 'Manager', 
                 'Country Manager', 'Region Manager', 'Partner', 'Senior Partner', 'C-level', 'CEO'],
    'Level': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary': [45000, 50000, 60000, 80000, 110000, 150000, 200000, 300000, 500000, 1000000]
}
df = pd.DataFrame(data)

# 2. Identifying Independent (X) and Target (y) variables
# We use 'Level' to predict 'Salary'
X = df[['Level']] 
y = df['Salary']

# 3. Split the variables into training and testing sets (7:3 ratio)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Print the sets
print("--- Training Set (70%) ---")
print("X_train:\n", X_train)
print("y_train:\n", y_train)

print("\n--- Testing Set (30%) ---")
print("X_test:\n", X_test)
print("y_test:\n", y_test)

# 5. Build a simple linear regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Output prediction check
print(f"\nModel Coefficient: {regressor.coef_[0]}")
print(f"Model Intercept: {regressor.intercept_}")



