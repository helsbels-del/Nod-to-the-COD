import streamlit as st

def page_summary_body():
    st.title("📚 Welcome to 'Nod to the COD'")

    st.markdown("""
    This dashboard explores trends and predictions of **Chemical Oxygen Demand (COD)** in wastewater treatment.

    ---
    """)

    st.subheader("📘 Project Terms & Jargon")

    st.info("""
    - **COD** (Chemical Oxygen Demand): A measure of the amount of oxygen required to oxidize organic and inorganic compounds in water.
    - **BOD** (Biological Oxygen Demand): A related metric showing oxygen demand from biological processes.
    - **TN** (Total Nitrogen): Total amount of nitrogen, important for nutrient loading and treatment.
    - **Coagulants**: Chemicals used to remove solids and organics from water in the treatment process.
    - **Outflow/Inflow**: The volume of water leaving or entering the treatment system.
    - **Feature Importance**: A score showing how much a variable contributes to predicting COD levels.
    """)

    st.subheader("📦 Dataset Overview")
    st.markdown("""
    The dataset represents operational and environmental data from a full-scale wastewater treatment plant.
    It includes:
    - Water quality measures (COD, BOD, TN, etc.)
    - Weather data (temperature, rainfall, wind)
    - Plant inflow and outflow volumes
    """)

    st.subheader("🎯 Business Objectives")
    st.markdown("""
    1. Identify key variables that influence COD levels throughout the year.
    2. Enable predictive modelling to support optimal chemical dosing and regulatory compliance.
    """)
