import streamlit as st
import pandas as pd
import numpy as np
from fraud_pipeline import create_synthetic_transaction_data, train_fraud_model

st.set_page_config(page_title="Fraud Detection Engine", layout="wide")

st.title("Financial Fraud Detection Security Engine")

@st.cache_resource
def load_and_train_system_pipeline():
    data = create_synthetic_transaction_data(1500)
    model = train_fraud_model(data)
    return model, data

model, data = load_and_train_system_pipeline()

st.subheader("Real-Time Single Transaction Risk Analyzer")

c1, c2 = st.columns(2)
with c1:
    input_amount = st.number_input("Transaction Amount ($):", min_value=0.0, value=50.0, step=5.0)
with c2:
    input_risk = st.slider("System Behavioral Risk Profile Score (0-100):", min_value=0.0, max_value=100.0, value=25.0)

if st.button("Evaluate Transaction Risk"):
    features = np.array([[input_amount, input_risk]])
    prediction = model.predict(features)
    prediction_proba = model.predict_proba(features)[0][1]
    
    st.markdown("---")
    if prediction[0] == 1 or prediction_proba > 0.70:
        st.error(f"High Risk Alert Status: Transaction Flagged as FRAUDULENT (Probability Score: {prediction_proba * 100:.1f}%)")
    else:
        st.success(f"Clear Status Verification: Transaction Authorized Successfully (Probability Score: {prediction_proba * 100:.1f}%)")

st.markdown("---")
st.subheader("System Training Dataset Metrics Registry")
st.dataframe(data.head(15), use_container_width=True)