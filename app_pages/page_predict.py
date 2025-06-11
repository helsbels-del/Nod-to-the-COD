import streamlit as st
import pandas as pd
import joblib

def page_predict_body():
    st.title("🔮 COD Prediction Tool")

    model = joblib.load("outputs/models/final_model.pkl")
    features = model.feature_names_in_

    st.markdown("Enter values below to estimate COD levels:")

    user_input = {}
    for feature in features:
        user_input[feature] = st.number_input(f"{feature}", value=0.0)

    if st.button("Predict COD"):
        input_df = pd.DataFrame([user_input])
        prediction = model.predict(input_df)[0]
        st.success(f"Estimated COD: **{prediction:.2f} mg/L**")
