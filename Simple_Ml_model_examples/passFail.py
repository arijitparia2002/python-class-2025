import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
 #Student pass/fail prediction
data = {
    'Study_Hours': [2, 3, 5, 7, 8, 1, 4, 6, 9, 10],
    'Attendance': [60, 70, 80, 90, 95, 50, 75, 85, 98, 100],
    'Previous_Score': [45, 55, 65, 75, 85, 40, 60, 70, 90, 95],
    'Pass': [0, 0, 1, 1, 1, 0, 1, 1, 1, 1]  # 0 = Fail, 1 = Pass
 }

df = pd.DataFrame(data)
 # Prepare
X = df[['Study_Hours', 'Attendance', 'Previous_Score']]
y = df['Pass']
 # Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
 # Train Decision Tree
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
 # Predict
y_pred = model.predict(X_test)
 # Evaluate
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
 # Feature importance
importance = model.feature_importances_
features = X.columns
print("\nFeature Importance:")

for feature, imp in zip(features, importance):
     print(f"{feature}: {imp:.3f}")
 # Predict for new student


new_student = pd.DataFrame({
    'Study_Hours': [6],
    'Attendance': [80],
    'Previous_Score': [70]
 })


prediction = model.predict(new_student)
print(f"\nNew student will: {'PASS' if prediction[0] == 1 else 'FAIL'}")