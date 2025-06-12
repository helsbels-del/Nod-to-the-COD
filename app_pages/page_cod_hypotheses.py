import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def page_cod_hypotheses_body():
    st.title("🧪 Project Hypotheses and Validation")

    st.markdown("This page outlines key project hypotheses, how they were tested, and whether they were supported by the data.")

    # Hypothesis 1 with checkbox toggle and live plot
    with st.expander("📌 Hypothesis 1 — Temperature and Feature Correlations with COD"):
        st.markdown("""
        **Hypothesis:** Higher temperatures are associated with lower COD levels due to increased microbial activity.

        - 🔍 **Evaluation:** Scatterplot and correlation analysis
        """)

        # COD vs Temperature
        if st.checkbox("📈 Show plot and correlation for COD vs Temperature"):
            df = pd.read_csv("outputs/datasets/collection/Data-Melbourns_F_fixed.csv", parse_dates=["date"])
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.scatterplot(x="Average Temperature", y="Chemical Oxygen Demand", data=df, ax=ax)
            ax.set_title("COD vs Average Temperature")
            ax.set_xlabel("Average Temperature (°C)")
            ax.set_ylabel("Chemical Oxygen Demand (mg/L)")
            st.pyplot(fig)

            correlation = df["Average Temperature"].corr(df["Chemical Oxygen Demand"])
            st.markdown(f"**Correlation:** `{correlation:.2f}` — ❌ Weak correlation")

        # Custom feature correlation section
        st.markdown("### 📊 Try another feature vs COD")

        if st.checkbox("🔍 Show custom feature comparison with COD"):
            options = [col for col in df.columns if col not in ["Chemical Oxygen Demand", "date"]]
            selected = st.selectbox("Choose a feature to compare with COD:", options)

            fig2, ax2 = plt.subplots(figsize=(8, 6))
            sns.scatterplot(x=df[selected], y=df["Chemical Oxygen Demand"], ax=ax2)
            ax2.set_title(f"COD vs {selected}")
            ax2.set_xlabel(selected)
            ax2.set_ylabel("Chemical Oxygen Demand (mg/L)")
            st.pyplot(fig2)

            corr_dynamic = df[selected].corr(df["Chemical Oxygen Demand"])

            # Determine strength for interpretation
            if abs(corr_dynamic) > 0.7:
                emoji = "✅"
                label = "Strong correlation"
            elif abs(corr_dynamic) > 0.3:
                emoji = "⚠️"
                label = "Moderate correlation"
            else:
                emoji = "❌"
                label = "Weak or no correlation"

            st.markdown(f"**Correlation between `{selected}` and COD:** `{corr_dynamic:.2f}` — {emoji} {label}")

    # Other hypotheses
    with st.expander("📌 Hypothesis 2 — ML COD Prediction"):
        st.markdown("""
        **Hypothesis:** COD can be accurately predicted using operational and environmental data.

        - 🔍 **Type:** Predictive hypothesis  
        - 🧪 **Evaluation:** Trained Random Forest model on selected features  
        - ✅ **Result:** Model achieved high R² and performance, confirming the hypothesis.
        """)

    with st.expander("📌 Hypothesis 3 — Operational Clusters"):
        st.markdown("""
        **Hypothesis:** There are distinct operational profiles corresponding to COD levels.

        - 🔍 **Type:** Exploratory clustering  
        - 🧪 **Evaluation:** Clustering on treatment features reveals operational groupings  
        - ✅ **Result:** Supported — clusters align with COD patterns and may help detect anomalies.
        """)

    st.success("These hypotheses shaped the structure of the analysis and were evaluated using visualisation, machine learning, and statistical techniques.")
