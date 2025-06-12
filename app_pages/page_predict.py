import streamlit as st
import pandas as pd
import joblib

def page_predict_body():
    st.title("🔮 COD Prediction Tool")

    st.markdown("Enter treatment condition values below to estimate Chemical Oxygen Demand (COD) levels:")

    # Load model
    model = joblib.load("outputs/models/final_model.pkl")

    # Create 3 columns for cleaner layout
    col1, col2, col3 = st.columns(3)

    with col1:
        ammonia = st.number_input("Ammonia", value=0.0)

    with col2:
        bod = st.number_input("Biological Oxygen Demand", value=0.0)

    with col3:
        tn = st.number_input("Total Nitrogen", value=0.0)

    # Make prediction
    if st.button("Predict COD"):
        input_df = pd.DataFrame([{
            "Ammonia": ammonia,
            "Biological Oxygen Demand": bod,
            "Total Nitrogen": tn
        }])

        prediction = model.predict(input_df)[0]
        st.success(f"Estimated COD: **{prediction:.2f} mg/L**")

        # Interpret COD level
        if prediction < 500:
            st.success("✅ COD is low — good water quality. Treatment conditions appear well-optimised.")
        elif 500 <= prediction <= 1000:
            st.warning("⚠️ COD is moderate — within acceptable range, but monitor regularly.")
        else:
            st.error("🚨 COD is high — consider reviewing treatment inputs or operational conditions.")

        # Context box
        st.info("""
        Interpreting COD helps identify:
        - Potential risks of under-treatment or overload
        - Early warning signs before discharge violations
        - Opportunities to adjust dosing or maintenance strategies
        """)


