import streamlit as st

def page_summary_body():
    st.title("📚 Welcome to 'Nod to the COD'")
    st.markdown("""
    This dashboard explores trends and predictions of **Chemical Oxygen Demand (COD)** in wastewater treatment.

    ### Included Sections:
    - COD trends across the year 📈
    - Feature importance from machine learning models 🧠
    - A live prediction tool for COD levels 🔮

    **Project Goal:**  
    Help treatment facilities make data-driven decisions for efficient chemical dosing and regulation compliance.
    """)
