import streamlit as st

def page_cod_hypotheses_body():
    st.title("🧪 Hypotheses and Validation Strategies")

    st.markdown("This page outlines key hypotheses developed for the project and how they were evaluated during analysis.")

    with st.expander("📌 Hypothesis 1 — Conventional Analysis"):
        st.markdown("""
        **Hypothesis:** Higher temperatures are associated with lower COD levels due to increased microbial activity.

        - 🔍 **Type:** Correlation hypothesis (testable via EDA and regression)
        - 🧪 **How to Evaluate:** Correlation heatmaps, scatter plots, linear regression, p-value analysis
        - 💡 **Business Relevance:** Helps operators understand seasonal variation and adapt treatment schedules accordingly.
        """)

    with st.expander("📌 Hypothesis 2 — ML-Driven Prediction"):
        st.markdown("""
        **Hypothesis:** COD can be accurately predicted using operational and environmental data.

        - 🔍 **Type:** Predictive hypothesis (requires supervised ML)
        - 🧪 **How to Evaluate:** Train/test ML models, measure performance using R²
        - 💡 **Business Relevance:** Enables proactive chemical dosing and operational adjustments to maintain compliance.
        """)

    with st.expander("📌 Hypothesis 3 — Clustering for Operational Profiles"):
        st.markdown("""
        **Hypothesis:** There are distinct operational profiles in plant behaviour that correspond to specific COD clusters.

        - 🔍 **Type:** Exploratory hypothesis (requires unsupervised learning)
        - 🧪 **How to Evaluate:** Apply clustering (KMeans, DBSCAN), validate using silhouette score or Davies-Bouldin index
        - 💡 **Business Relevance:** Supports anomaly detection, process optimisation, and benchmarking of typical vs atypical behaviour.
        """)

    st.success("These hypotheses informed the structure of the analysis and model design, aligning technical exploration with real operational goals.")
