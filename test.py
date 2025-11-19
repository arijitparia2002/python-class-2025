import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
 # Step 2: Create sample data
data = {
    'Age': [25, 30, 35, 40, 45, 50, 22, 28, 33, 38],
    'Income': [30000, 50000, 60000, 80000, 90000, 100000, 25000, 45000, 55000, 75000],
    'Purchased': [0, 0, 1, 1, 1, 1, 0, 0, 1, 1]
 }
df = pd.DataFrame(data)
 # Step 3: Prepare features and labels
X = df[['Age', 'Income']]  # Features
y = df['Purchased']         # Labels
 # Step 4: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
 # Step 5: Create model
model = LogisticRegression()
 # Step 6: Train model
model.fit(X_train, y_train)
 # Step 7: Make predictions
y_pred = model.predict(X_test)
 # Step 8: Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100}%")


new_customers = pd.DataFrame({
    'Age': [29, 41, 36],
    'Income': [48000, 82000, 61000]
})

predictions = model.predict(new_customers)
print(predictions)
for i, pred in enumerate(predictions):
    print(f"Customer {i+1} prediction (0=Not Purchased, 1=Purchased): {pred}")