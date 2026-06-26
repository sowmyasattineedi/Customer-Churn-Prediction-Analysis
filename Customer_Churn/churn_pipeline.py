import os
import pandas as pd
from sqlalchemy import create_engine
import urllib.parse
from sklearn.ensemble import RandomForestClassifier
from dotenv import load_dotenv

load_dotenv()

db_user = "root"
db_pass = os.getenv("DB_PASSWORD") 
db_host = "localhost"
db_port = "3306"
db_name = "churn_db"

try:
  
    encoded_pass = urllib.parse.quote_plus(db_pass)
    conn_str = f"mysql+pymysql://{db_user}:{encoded_pass}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(conn_str)
    
    df = pd.read_sql("SELECT * FROM customer_metrics", con=engine)
    
    df['is_month_to_month'] = df['contract_type'].apply(lambda x: 1 if x == 'Month-to-month' else 0)
    
    features = ['tenure_months', 'monthly_charges', 'total_charges', 'tech_support_user', 'is_month_to_month']
    X = df[features]
    y = df['churned']
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    df['churn_probability'] = pd.Series(model.predict_proba(X)[:, 1]).round(2)
    df['predicted_churn'] = model.predict(X)
    
    output_file = "customer_churn_predictions.csv"
    df.to_csv(output_file, index=False)
    print(f"\nPipeline complete! Target file generated: {output_file}")

except Exception as e:
    print(f"\nPipeline execution failure: {str(e)}")