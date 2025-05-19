import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
import os

MODEL_PATH = "core/risk_model.joblib"

# Only load the trained model at import time
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None

def predict_risk(input_data):
    if model is None:
        raise RuntimeError("Model not loaded. Train the model first.")
    df = pd.DataFrame([input_data])
    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]  # Probability of risk=1
    return int(pred), float(prob)

if __name__ == "__main__":
    # Only run this block to (re)train the model!
    data = pd.read_csv(r"../labeled_patient_data.csv")
    X = data[['age', 'bp', 'heart_rate', 'comorbidity_score']]
    y = data['risk']
    model = DecisionTreeClassifier()
    model.fit(X, y)
    os.makedirs("core", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print("Model trained and saved to core/risk_model.joblib")

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

