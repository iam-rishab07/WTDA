'''
Q. 2)Create ‘User’ Data set having 5 columns namely: User ID, Gender, Age, Estimated Salary

and urchased. Build a logistic regression model that can predict whether on the given

parameter a person will buy a car or not
'''

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression

# # 1. Create the 'User' Dataset
# data = {
#     'User ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     'Gender': [1, 1, 0, 0, 1, 1, 0, 0, 1, 0], # 1 for Male, 0 for Female
#     'Age': [19, 35, 26, 27, 19, 27, 32, 25, 33, 45],
#     'Estimated Salary': [19000, 20000, 43000, 57000, 76000, 58000, 82000, 32000, 69000, 65000],
#     'Purchased': [0, 0, 0, 1, 1, 0, 1, 0, 1, 1]
# }
# df = pd.DataFrame(data)

# # 2. Identify Independent (X) and Target (y) variables
# # X = Gender, Age, Salary | y = Purchased
# X = df[['Gender', 'Age', 'Estimated Salary']]
# y = df['Purchased']

# # 3. Split into Training and Testing sets (7:3 ratio)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# # 4. Build and Train the Logistic Regression Model
# lr = LogisticRegression()
# lr.fit(X_train, y_train)

# # 5. Predict a single observation (Female=0, Age=30, Salary=87000)
# observation = [[0, 30, 87000]]
# prediction = lr.predict(observation)
# print("Single Prediction:", prediction)

# # 6. Predict multiple observations
# observations = [[0, 30, 87000], [1, 50, 45000], [1, 22, 30000]]
# predictions = lr.predict(observations)
# print("Multiple Predictions:", predictions)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# 1. Create Dataset
data = {
    'Gender': [1, 1, 0, 0, 1, 1, 0, 0, 1, 0], 
    'Age': [19, 35, 26, 27, 19, 27, 32, 25, 33, 45],
    'Salary': [19000, 20000, 43000, 57000, 76000, 58000, 82000, 32000, 69000, 65000],
    'Purchased': [0, 0, 0, 1, 1, 0, 1, 0, 1, 1]
}
df = pd.DataFrame(data)

# 2. Split Features (X) and Target (y)
X = df[['Gender', 'Age', 'Salary']]
y = df['Purchased']

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 4. Build and Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# 5. Predict for new data (e.g., Female=0, Age=30, Salary=87000)
pred = model.predict([[0, 30, 87000]])
print("Prediction for person:", "Will Buy" if pred[0] == 1 else "Will Not Buy")

# 6. Accuracy (Optional but good for marks)
print("Model Accuracy:", model.score(X_test, y_test))