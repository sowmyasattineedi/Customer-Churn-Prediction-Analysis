import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def create_synthetic_transaction_data(num_records=1000):
    np.random.seed(42)
    
    amounts = np.random.exponential(scale=100, size=num_records)
    risk_scores = np.random.uniform(0, 100, size=num_records)
    
    # Base mapping for fraud flags
    is_fraud = np.where((amounts > 300) & (risk_scores > 70), 1, 0)
    
    # Inject minority fraud cases for balancing scenarios
    fraud_indices = np.random.choice(num_records, size=int(num_records * 0.05), replace=False)
    is_fraud[fraud_indices] = 1
    amounts[fraud_indices] = amounts[fraud_indices] * 3
    risk_scores[fraud_indices] = np.random.uniform(75, 100, size=len(fraud_indices))

    df = pd.DataFrame({
        'Transaction_Amount': amounts,
        'Risk_Score': risk_scores,
        'Is_Fraud': is_fraud
    })
    return df

def train_fraud_model(df):
    X = df[['Transaction_Amount', 'Risk_Score']]
    y = df['Is_Fraud']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Production Model Pipeline Initialization
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    
    print("Model Evaluation Assessment:")
    print(f"Accuracy Score Metrics: {accuracy_score(y_test, predictions) * 100:.2f}%")
    print("\nClassification Report Metrics:")
    print(classification_report(y_test, predictions))
    
    return model

if __name__ == "__main__":
    dataset = create_synthetic_transaction_data(1200)
    trained_model = train_fraud_model(dataset)