import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime, timedelta

def generate_historical_sales_data(days=730):
    np.random.seed(42)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    date_range = [start_date + timedelta(days=x) for x in range(days)]
    products = [101, 102, 103, 104]
    regions = ['North', 'South', 'East', 'West']
    
    records = []
    
    for idx, current_date in enumerate(date_range):
        base_modifier = 1.0 + (idx / 1000.0)
        day_of_week = current_date.weekday()
        weekend_boost = 1.3 if day_of_week >= 5 else 1.0
        
        for prod_id in products:
            base_qty = np.random.randint(5, 25)
            units_sold = int(base_qty * base_modifier * weekend_boost)
            
            price_map = {101: 1200.00, 102: 45.00, 103: 250.00, 104: 65.00}
            unit_price = price_map[prod_id]
            revenue = units_sold * unit_price
            
            records.append({
                'transaction_id': f"TXN-SALE-{idx:05d}-{prod_id}",
                'sale_date': current_date.strftime('%Y-%m-%d'),
                'product_id': prod_id,
                'units_sold': units_sold,
                'store_region': np.random.choice(regions),
                'total_revenue': round(revenue, 2)
            })
            
    df = pd.DataFrame(records)
    return df

if __name__ == "__main__":
    print("Initializing sales pipeline tracking matrix...")
    sales_df = generate_historical_sales_data()
    
    output_path = "sales_historical_records.csv"
    sales_df.to_csv(output_path, index=False)
    print(f"Pipeline successfully compiled! Saved {len(sales_df)} rows to '{output_path}'.")