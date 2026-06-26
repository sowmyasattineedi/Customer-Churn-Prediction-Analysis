import streamlit as st
import pandas as pd

st.title("Customer Churn ML Predictions Output")
st.write("Here is the live interactive output from your Python pipeline:")

df = pd.read_csv("customer_churn_predictions.csv")
st.dataframe(df)