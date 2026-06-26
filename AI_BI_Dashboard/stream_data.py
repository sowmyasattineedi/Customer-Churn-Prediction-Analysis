import pandas as pd
import numpy as np
import time
from datetime import datetime

def generate_live_stream_data(num_records=100):
    np.random.seed(int(time.time()))
    
    categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty']
    regions = ['North', 'East', 'South', 'West']
    payment_methods = ['Credit Card', 'PayPal', 'UPI', 'Debit Card']
    
    data = {
        'Transaction_ID': [f"TXN-{10000 + i}" for i in range(num_records)],
        'Timestamp': [datetime.now().strftime('%Y-%m-%d %H:%M:%S') for _ in range(num_records)],
        'Customer_ID': [f"CUST-{np.random.randint(100, 999)}" for _ in range(num_records)],
        'Category': np.random.choice(categories, num_records),
        'Amount': np.round(np.random.uniform(10.0, 500.0, num_records), 2),
        'Quantity': np.random.randint(1, 5, num_records),
        'Region': np.random.choice(regions, num_records),
        'Payment_Method': np.random.choice(payment_methods, num_records)
    }
    
    df = pd.DataFrame(data)
    df['Total_Revenue'] = df['Amount'] * df['Quantity']
    return df

if __name__ == "__main__":
    sample_df = generate_live_stream_data(5)
    print(sample_df.head())