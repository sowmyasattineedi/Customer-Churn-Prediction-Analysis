import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Sales Forecasting Dashboard", layout="wide")

st.title("Sales Forecasting Dashboard")

def load_data():
    df = pd.read_csv("sales_historical_records.csv")
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    return df

try:
    data = load_data()
    
    daily_sales = data.groupby('sale_date')['total_revenue'].sum().reset_index()
    daily_sales = daily_sales.sort_values('sale_date')
    
    daily_sales['day_index'] = np.arange(len(daily_sales))
    
    X = daily_sales[['day_index']]
    y = daily_sales['total_revenue']
    
    model = LinearRegression()
    model.fit(X, y)
    
    future_days = 30
    last_day_index = daily_sales['day_index'].max()
    future_indices = np.arange(last_day_index + 1, last_day_index + 1 + future_days).reshape(-1, 1)
    
    future_predictions = model.predict(future_indices)
    
    last_date = daily_sales['sale_date'].max()
    future_dates = [last_date + timedelta(days=int(i)) for i in range(1, future_days + 1)]
    
    forecast_df = pd.DataFrame({
        'sale_date': future_dates,
        'predicted_revenue': np.round(future_predictions, 2)
    })
    
    col1, col2, col3 = st.columns(3)
    
    total_historical = daily_sales['total_revenue'].sum()
    avg_daily_revenue = daily_sales['total_revenue'].mean()
    projected_next_month = forecast_df['predicted_revenue'].sum()
    
    col1.metric(label="Total Historical Revenue", value=f"${total_historical:,.2f}")
    col2.metric(label="Average Daily Revenue", value=f"${avg_daily_revenue:,.2f}")
    col3.metric(label="Projected Revenue (Next 30 Days)", value=f"${projected_next_month:,.2f}")
    
    st.subheader("Next 30 Days Revenue Forecast")
    
    display_forecast = forecast_df.copy()
    display_forecast['sale_date'] = display_forecast['sale_date'].dt.strftime('%Y-%m-%d')
    display_forecast.columns = ['Date', 'Predicted Revenue']
    
    st.dataframe(display_forecast, use_container_width=True, hide_index=True)
    
    st.subheader("Forecasted Trend")
    st.line_chart(forecast_df.set_index('sale_date'))
    
except FileNotFoundError:
    st.error("Historical data file not found. Please run the pipeline script first.")