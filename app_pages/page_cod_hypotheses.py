import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

def page_cod_hypotheses_body():
    st.title("🧪 Project Hypotheses and Validation")
    st.markdown("This page outlines key project hypotheses, how they were tested, and whether they were supported by the data.")

    df = pd.read_csv("outputs/datasets/collection/cleaned_cod_data.csv")

    # Hypothesis 1 — Temperature and Feature Correlations
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
            st.markdown(f"""
            - 📉 **Correlation coefficient:** `{correlation:.2f}`  
            - ❌ **Conclusion:** Not supported. The correlation is weak, with no clear trend.
            """)

       

    # Hypothesis 2 — ML Prediction
    with st.expander("📌 Hypothesis 2 — COD Can Be Predicted Using ML"):
        st.markdown("""
        **Hypothesis:** COD levels can be accurately predicted using operational and environmental features.

        - 📊 **Evaluation:** Regression and classification models were trained  
        - 🧠 **Model (Regression):** Random Forest Regressor  
        - 🧠 **Model (Classification):** Random Forest Classifier
        """)

        if st.checkbox("🔍 Show model performance metrics"):
            st.markdown("#### 🧮 Regression Results")
            st.markdown("""
            - **Tuned MAE:** 49.44  
            - **Tuned RMSE:** 73.60  
            - **Tuned R²:** 0.71 ✅  
            """)
            st.markdown("#### 🧮 Classification Results (Confusion Matrix)")
            st.markdown("""
            ```
            | True ↓ / Pred → | Low | Med | High |
            |------------------|-----|-----|------|
            | Low              | 54  |  0  | 31   |
            | Med              | 0   |  4  | 5    |
            | High             | 22  |  1  | 160  |
            ```
            - This shows the model's predictions across 3 COD classes
            """)

        if st.checkbox("📈 Show Feature Importance Plot"):
            model = joblib.load("outputs/models/final_model.pkl")
            features = model.feature_names_in_
            importances = model.feature_importances_

            imp_df = pd.DataFrame({
                "Feature": features,
                "Importance": importances
            }).sort_values(by="Importance", ascending=True)

            fig, ax = plt.subplots(figsize=(8, 6))
            sns.barplot(x="Importance", y="Feature", data=imp_df, ax=ax)
            ax.set_title("Feature Importance for COD Prediction")
            ax.set_xlabel("Relative Feature Importance (Gini)")
            st.pyplot(fig)

        st.success("✅ Hypothesis supported. COD levels were predicted with good accuracy using Random Forest models.")

    # Hypothesis 3 — Clustering
    with st.expander("📌 Hypothesis 3 — Operational Clustering"):
        st.markdown("""
        **Hypothesis:** There are distinct operational profiles in the dataset that correspond to specific COD behaviour clusters.

        - 🔍 **Type:** Exploratory hypothesis (unsupervised learning)  
        - 🧪 **Evaluation:** Clustering applied to operational features (e.g., KMeans)  
        - 📊 **Goal:** Identify patterns in treatment behaviour that influence COD
        """)

        if st.checkbox("📉 Show cluster visualisation and interpretation"):
            df_cluster = pd.read_csv("outputs/datasets/cluster_data.csv")

            fig, ax = plt.subplots(figsize=(8, 6))
            sns.scatterplot(
                x="PCA1", y="PCA2", hue="Cluster",
                data=df_cluster, palette="Set2", s=100,
                edgecolor="black", ax=ax
            )
            ax.set_title("Operational Clusters (PCA Projection, Color = Cluster)")
            ax.set_xlabel("PCA Component 1")
            ax.set_ylabel("PCA Component 2")
            st.pyplot(fig)

            if "Chemical Oxygen Demand" in df_cluster.columns:
                st.markdown("#### 📌 Average COD per Cluster:")
                summary = (
                    df_cluster.groupby("Cluster")["Chemical Oxygen Demand"]
                    .agg(["count", "mean"])
                    .rename(columns={"count": "Samples", "mean": "Avg COD (mg/L)"})
                    .round(2)
                )

                def label_cod(value):
                    if value < 600:
                        return "Low COD"
                    elif value < 900:
                        return "Moderate COD"
                    else:
                        return "High COD"

                summary["COD Label"] = summary["Avg COD (mg/L)"].apply(label_cod)
                st.dataframe(summary)

                st.markdown("#### 📊 Avg COD by Cluster")
                fig_bar, ax_bar = plt.subplots()
                sns.barplot(x=summary.index, y=summary["Avg COD (mg/L)"], palette="Set2", ax=ax_bar)
                ax_bar.set_xlabel("Cluster")
                ax_bar.set_ylabel("Avg COD (mg/L)")
                ax_bar.set_title("Average COD by Cluster")
                st.pyplot(fig_bar)

        st.success("✅ Hypothesis supported. Operational clusters highlight behavioural patterns related to COD, useful for monitoring and optimisation.")
