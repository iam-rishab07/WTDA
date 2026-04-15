import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 1. Load Data
df = pd.read_csv('student_scores.csv')
X = df.iloc[:, :-1]  # All columns except last
y = df.iloc[:, -1]   # Last column

# 2. Split (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 3. Model Training
model = LogisticRegression()
model.fit(X_train, y_train)

# 4. Evaluation
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))