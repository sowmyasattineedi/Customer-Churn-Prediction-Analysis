import os
import pandas as pd
from sqlalchemy import create_engine
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

db_user = "root"
db_pass = os.getenv("DB_PASSWORD") 
db_host = "localhost"
db_port = "3306"
db_name = "dashboard_db"

try:
    encoded_pass = urllib.parse.quote_plus(db_pass)
    
    conn_str = f"mysql+pymysql://{db_user}:{encoded_pass}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(conn_str)
    
    query = "SELECT * FROM product_sales"
    df = pd.read_sql(query, con=engine)
    
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['profit_margin_pct'] = round((df['profit'] / df['sales']) * 100, 2)
    df['avg_order_value'] = round(df['sales'] / df['orders'], 2)
    
    output_file = "power_bi_cleaned_sales.csv"
    df.to_csv(output_file, index=False)
    print(f"Data pipeline complete. Output saved to: {output_file}")

except Exception as e:
    print(f"Pipeline processing failure: {str(e)}")