import streamlit as st


def page_summary_body():
    st.title("📚 Welcome to 'Nod to the COD'")

    st.markdown("""
    This dashboard explores trends and predictions of **Chemical Oxygen Demand
                 (COD)** in wastewater treatment.

    ---
    """)

    st.subheader("📘 Project Terms & Jargon")

    st.info("""
    - **COD** (Chemical Oxygen Demand): A measure of the amount of oxygen
             required to oxidize organic and inorganic compounds in water.
    - **BOD** (Biological Oxygen Demand): A related metric showing oxygen
             demand from biological processes.
    - **TN** (Total Nitrogen): Total amount of nitrogen, important for nutrient
             loading and treatment.
    - **Coagulants**: Chemicals used to remove solids and organics from water
             in the treatment process.
    - **Outflow/Inflow**: The volume of water leaving or entering the treatment
             system.
    - **Feature Importance**: A score showing how much a variable contributes
             to predicting COD levels.
    """)

    st.subheader("📦 Dataset Overview")
    st.markdown
    st.markdown("""
    The dataset represents operational and environmental data from a full-scale
    wastewater treatment plant.
    It includes:
    - Water quality measures (COD, BOD, TN, etc.)
    - Weather data (temperature, rainfall, wind)
    - Plant inflow and outflow volumes
    """)

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/helsbels-del/Nod-to-the-COD).")

    st.subheader("🎯 Business Requirements")

    st.success("""
        1. **Understand trends in COD levels over time**  
          Identify seasonal patterns and operational influences.  

        2. **Predict future COD levels using ML models**  
          Support proactive treatment decisions.  

        3. **Test specific hypotheses related to operational/environmental drivers**  
          Validate assumptions with data-backed insights.  
        """)

