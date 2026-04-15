# Q. 2)Build a simple linear regression model for Fish Species Weight
# Prediction

import pandas as pd
import random
from sklearn.linear_model import LinearRegression

# 1. Create the dataset (Length of fish to predict Weight)
data = []
for i in range(50):
    length = random.randint(10, 50)
    # Weight is roughly length * 2 plus some random noise
    weight = (length * 2) + random.randint(-5, 5)
    data.append([length, weight])

df = pd.DataFrame(data, columns=['Length', 'Weight'])

# 2. Identify Independent (X) and Target (y) variables
# X must be 2D [[ ]], y can be 1D
X = df[['Length']] 
y = df['Weight']

# 3. Create and train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# 4. Predict the weight of a fish with a length of 30cm
new_fish_length = [[30]] 
predicted_weight = model.predict(new_fish_length)

print("--- Fish Weight Prediction ---")
print(f"Predicted weight for length 30: {predicted_weight[0]:.2f}")

# 5. Print Model Parameters
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)