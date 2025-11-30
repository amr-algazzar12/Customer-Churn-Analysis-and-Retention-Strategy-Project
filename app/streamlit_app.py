# Fixed Streamlit App with Correct Feature Alignment
# (Paste into app/streamlit_app.py)

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
MODEL_PATH = PROJECT_ROOT / 'models' / 'random_forest_model.pkl'
SCALER_PATH = PROJECT_ROOT / 'models' / 'scaler.pkl'
ENCODED_COLS_PATH = PROJECT_ROOT / 'models' / 'encoded_columns.pkl'
TEMPLATE_PATH = PROJECT_ROOT / 'models' / 'input_template.pkl'

st.set_page_config(page_title="Churn Predictor", page_icon="📊", layout="wide")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

@st.cache_resource
def load_scaler():
    return joblib.load(SCALER_PATH)

@st.cache_resource
def load_encoded_cols():
    return joblib.load(ENCODED_COLS_PATH)

@st.cache_resource
def load_template():
    return joblib.load(TEMPLATE_PATH)

model = load_model()
scaler = load_scaler()
encoded_cols = load_encoded_cols()
template = load_template()

st.markdown('<h1 style="text-align:center;color:#1f77b4">📊 Customer Churn Predictor</h1>', unsafe_allow_html=True)
st.markdown("---")

st.header("🔮 Predict Churn Risk")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior = st.selectbox("Senior", ["No", "Yes"])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])

    tenure = st.slider("Months", 0, 72, 12)
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("Paperless Billing", ["No", "Yes"])
    payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

with col2:
    phone = st.selectbox("Phone", ["No", "Yes"])
    internet = st.selectbox("Internet", ["No", "DSL", "Fiber optic"])

    tech = st.selectbox("Tech Support", ["No", "Yes"]) if internet != "No" else "No"

    monthly = st.number_input("Monthly ($)", 18.0, 120.0, 70.0, 5.0)
    total = st.number_input("Total ($)", 0.0, 10000.0, float(monthly * tenure), 50.0)
    cltv = st.number_input("CLTV ($)", 2000, 6500, 4400, 100)

if st.button("🔍 Predict", type="primary", use_container_width=True):

    raw_input = {
        'Count': 1,
        'Country': 0,
        'State': 0,
        'City': 562,
        'Zip Code': 90210,
        'Lat Long': 902,
        'Latitude': 34.0,
        'Longitude': -118.0,
        'Gender': 1 if gender == "Male" else 0,
        'Senior Citizen': 1 if senior == "Yes" else 0,
        'Partner': 1 if partner == "Yes" else 0,
        'Dependents': 1 if dependents == "Yes" else 0,
        'Tenure Months': tenure,
        'Phone Service': 1 if phone == "Yes" else 0,
        'Multiple Lines': 0,
        'Internet Service': 2 if internet == "Fiber optic" else (1 if internet == "DSL" else 0),
        'Online Security': 1,
        'Online Backup': 1,
        'Device Protection': 1,
        'Tech Support': 2 if tech == "Yes" else 1,
        'Streaming TV': 1,
        'Streaming Movies': 1,
        'Contract': 2 if contract == "Two year" else (1 if contract == "One year" else 0),
        'Paperless Billing': 1 if paperless == "Yes" else 0,
        'Payment Method': 3 if "Credit" in payment else (2 if "Bank" in payment else (1 if "Mailed" in payment else 0)),
        'Monthly Charges': monthly,
        'Total Charges': total,
        'CLTV': cltv
    }

    df_input = pd.DataFrame([raw_input])

    aligned = template.copy()
    for col in aligned.columns:
        aligned[col] = df_input[col] if col in df_input.columns else 0

    aligned_scaled = scaler.transform(aligned)

    pred = model.predict(aligned_scaled)[0]
    prob = model.predict_proba(aligned_scaled)[0][1] * 100

    st.markdown("### 📊 Results")
    colA, colB, colC = st.columns(3)

    with colA:
        st.metric("Will Churn?", "YES ❌" if pred == 1 else "NO ✅")
    with colB:
        st.metric("Risk Score", f"{prob:.1f}%")
    with colC:
        risk = "High 🚨" if prob > 70 else ("Medium ⚠️" if prob > 40 else "Low ✅")
        st.metric("Risk Level", risk)

    st.progress(int(min(prob, 100)))
