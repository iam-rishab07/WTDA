from sklearn.linear_model import LinearRegression

# 1. Dataset (Mileage as X, Price as y)
# Note: X must be a 2D array [[value]]
mileage = [[10], [20], [30], [40], [50], [60], [70], [80]]
price = [24, 19, 17, 13, 10, 7, 5, 2]

# 2. Build and Fit the model
model = LinearRegression()
model.fit(mileage, price)

# 3. Print the results (y = mx + c)
print('Intercept (c):', model.intercept_)
print('Coefficient (m):', model.coef_[0])

# 4. Predict prices for new mileages
new_mileage = [[25], [45], [65]]
predictions = model.predict(new_mileage)
print('Predicted prices:', predictions)