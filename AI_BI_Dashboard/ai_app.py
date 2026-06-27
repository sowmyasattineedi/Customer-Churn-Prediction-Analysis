import streamlit as st
import pandas as pd
import time
from stream_data import generate_live_stream_data

st.set_page_config(page_title="Business Intelligence Dashboard", layout="wide")

st.title("Real-Time Business Intelligence Dashboard")

if 'live_data' not in st.session_state:
    st.session_state.live_data = generate_live_stream_data(200)

if st.button("Refresh Stream Data"):
    st.session_state.live_data = generate_live_stream_data(200)

df = st.session_state.live_data

total_revenue = df['Total_Revenue'].sum()
total_sales = df['Quantity'].sum()
average_amount = df['Amount'].mean()

m1, m2, m3 = st.columns(3)
with m1:
    st.metric(label="Total Revenue", value=f"${total_revenue:,.2f}")
with m2:
    st.metric(label="Total Units Sold", value=f"{total_sales:,}")
with m3:
    st.metric(label="Average Transaction Value", value=f"${average_amount:.2f}")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Revenue by Category")
    category_summary = df.groupby('Category')['Total_Revenue'].sum().sort_values(ascending=False)
    st.bar_chart(category_summary)

with col2:
    st.subheader("Revenue by Region")
    region_summary = df.groupby('Region')['Total_Revenue'].sum()
    st.line_chart(region_summary)

st.subheader("Natural Language Query Interface")
user_query = st.text_input(
    "Enter metric query:", 
    placeholder="e.g., Which category has the highest revenue?"
)

if user_query:
    query_clean = user_query.lower().strip()
    
    if "category" in query_clean and any(x in query_clean for x in ["most", "best", "highest"]):
        top_cat = df.groupby('Category')['Total_Revenue'].sum().idxmax()
        top_cat_val = df.groupby('Category')['Total_Revenue'].sum().max()
        st.write(f"Top performing category: **{top_cat}** (${top_cat_val:,.2f})")
        
    elif "region" in query_clean and "north" in query_clean:
        north_val = df[df['Region'] == 'North']['Total_Revenue'].sum()
        st.write(f"North region total revenue: **${north_val:,.2f}**")
        
    elif "region" in query_clean and "south" in query_clean:
        south_val = df[df['Region'] == 'South']['Total_Revenue'].sum()
        st.write(f"South region total revenue: **${south_val:,.2f}**")
        
    elif "payment" in query_clean or "method" in query_clean:
        top_payment = df['Payment_Method'].value_counts().idxmax()
        st.write(f"Primary payment method: **{top_payment}**")
        
    elif "total revenue" in query_clean:
        st.write(f"Aggregate system revenue: **${total_revenue:,.2f}**")
        
    else:
        st.write("Query did not match standard intent structures. Please use verified criteria fields.")

st.subheader("Transaction Log Stream")
st.dataframe(df.head(25), use_container_width=True)