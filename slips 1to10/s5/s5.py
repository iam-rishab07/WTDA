# Q. 2)Use the iris dataset. Write a Python program to view some basic statistical details like
# percentile,
# Mean, std etc. Of the species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris-virginica’. Apply logistic
# regression
# On the dataset to identify different species (setosa, versicolor, verginica) of Iris flowers
# given just 4
# Features: sepal and petal lengths and widths.. Find the accuracy of the
# model. 

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Load the iris dataset
iris = load_iris()

# 2. Create a dataframe
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# 3. View basic statistical details (describe() handles mean, std, percentiles)
print("--- Statistical details of Iris-setosa ---")
print(df[df['target'] == 0].describe())

print("\n--- Statistical details of Iris-versicolor ---")
print(df[df['target'] == 1].describe())

print("\n--- Statistical details of Iris-virginica ---")
print(df[df['target'] == 2].describe())

# 4. Split the data into training and testing sets (80:20 ratio)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Fit a logistic regression model
# max_iter is increased to ensure the model converges
logreg = LogisticRegression(max_iter=200)
logreg.fit(X_train, y_train)

# 6. Make predictions and find accuracy
y_pred = logreg.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\n" + "="*40)
print(f"Accuracy of the Logistic Regression model: {accuracy * 100}%")
print("="*40)