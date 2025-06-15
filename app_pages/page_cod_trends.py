import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.dates as mdates


def page_cod_trends_body():
    st.title("📊 COD Trends & Analysis")
    st.markdown("Explore how COD levels vary over time and"
                " relate to other treatment conditions.")

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
        # Only include numeric features
        numeric_features = df.select_dtypes(include='number').columns
        features = [col for col in numeric_features if col not in
                    ["Chemical Oxygen Demand"]]
        selected_feature = st.selectbox(
            "Choose a feature to compare with COD:", features)

        fig2, ax2 = plt.subplots()
        sns.scatterplot(data=df, x=selected_feature,
                        y="Chemical Oxygen Demand",
                        ax=ax2, alpha=0.5)
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
    

        # Convert Period to Timestamp for better formatting
        df['Month_Parsed'] = pd.to_datetime(df['date']).dt.to_period("M").dt.to_timestamp()
        monthly_avg = df.groupby("Month_Parsed")["Chemical Oxygen Demand"].mean()

        fig, ax = plt.subplots()

        # Raw COD trend
        ax.plot(df["Month_Parsed"], df["Chemical Oxygen Demand"], label="Chemical Oxygen Demand", color="gray", linewidth=1)

        # Monthly average
        monthly_avg = df.groupby("Month_Parsed")["Chemical Oxygen Demand"].mean()
        ax.plot(monthly_avg.index, monthly_avg.values, label="Monthly Avg", linestyle="--", color="#1f77b4")

        # Rolling average (3-month)
        rolling_avg = df.set_index("Month_Parsed")["Chemical Oxygen Demand"].rolling(3).mean()
        ax.plot(rolling_avg.index, rolling_avg.values, label="3-Month Rolling Avg", color="red", linewidth=1.0)

        # Formatting
        ax.set_title("Average COD by Month", fontsize=14, fontweight='bold')
        ax.set_ylabel("COD (mg/L)")
        ax.set_xlabel("Month")
        ax.legend(loc="upper right")
        ax.grid(True, linestyle='--', alpha=0.3)
        fig.autofmt_xdate()
        st.pyplot(fig)

        st.caption("🔍 COD levels show seasonal fluctuations with peaks and troughs — useful for informing proactive planning.")



    st.markdown("---")
    st.markdown("### 🔥 Correlation Heatmap")
    with st.expander("View correlation heatmap"):
        fig4, ax4 = plt.subplots(figsize=(10, 8))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm",
                    fmt=".2f", ax=ax4)
        ax4.set_title("Feature Correlation Heatmap")
        st.pyplot(fig4)

    st.markdown("---")
    st.markdown("✅ Use these insights to inform your model and explore"
                " hypothesis relationships.")
