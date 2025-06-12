import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def page_cod_trends_body():
    st.title("📊 COD Trends & Analysis")
    st.markdown("Explore how COD levels vary over time and relate to other treatment conditions.")

    df = pd.read_csv("outputs/datasets/collection/cleaned_cod_data.csv")

    st.markdown("### 📅 Monthly COD Distribution")
    with st.expander("View monthly COD boxplot"):
        fig1, ax1 = plt.subplots()
        sns.boxplot(data=df, x="Month", y="Chemical Oxygen Demand", ax=ax1)
        ax1.set_title("COD Distribution by Month")
        ax1.set_ylabel("COD (mg/L)")
        st.pyplot(fig1)

    st.markdown("---")
    st.markdown("### 📌 Feature vs COD Scatterplot")
    with st.expander("Explore scatterplot and correlation"):
        features = [col for col in df.columns if col not in ["Chemical Oxygen Demand", "Month", "Cluster"]]
        selected_feature = st.selectbox("Choose a feature to compare with COD:", features)

        fig2, ax2 = plt.subplots()
        sns.scatterplot(data=df, x=selected_feature, y="Chemical Oxygen Demand", ax=ax2, alpha=0.5)
        ax2.set_title(f"COD vs {selected_feature}")
        st.pyplot(fig2)

        corr = df["Chemical Oxygen Demand"].corr(df[selected_feature])
        st.markdown(f"**Correlation: {corr:.2f}**")
        if abs(corr) > 0.6:
            st.success("✅ Strong correlation.")
        elif abs(corr) > 0.3:
            st.warning("⚠️ Moderate correlation.")
        else:
            st.info("ℹ️ Weak correlation.")

    st.markdown("---")
    st.markdown("### 🌡️ COD Time Trend")
    with st.expander("View average monthly COD over time"):
        if "date" in df.columns:
            df['Month_Parsed'] = pd.to_datetime(df['date']).dt.to_period("M")
            monthly_avg = df.groupby("Month_Parsed")["Chemical Oxygen Demand"].mean()
            fig3, ax3 = plt.subplots()
            monthly_avg.plot(ax=ax3)
            ax3.set_title("Average COD by Month")
            ax3.set_ylabel("COD (mg/L)")
            st.pyplot(fig3)
        else:
            st.warning("Date column not found to calculate monthly average.")

    st.markdown("---")
    st.markdown("### 🔥 Correlation Heatmap")
    with st.expander("View correlation heatmap"):
        fig4, ax4 = plt.subplots(figsize=(10, 8))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", ax=ax4)
        ax4.set_title("Feature Correlation Heatmap")
        st.pyplot(fig4)

    st.markdown("---")
    st.markdown("✅ Use these insights to inform your model and explore hypothesis relationships.")
