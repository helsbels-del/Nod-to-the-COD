import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def page_cod_trends_body():
    st.title("📈 COD Trends by Time and Conditions")

    # Load dataset
    df = pd.read_csv("outputs/datasets/collection/cleaned_cod_data.csv")

    st.markdown("This section explores how **Chemical Oxygen Demand (COD)** changes over time and under different operational or environmental conditions.")

    # --- Monthly COD Distribution ---
    st.subheader("📦 COD Levels by Month")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.boxplot(x="Month", y="Chemical Oxygen Demand", data=df, ax=ax1)
    ax1.set_title("COD Distribution by Month")
    ax1.set_ylabel("COD (mg/L)")
    st.pyplot(fig1)

    # --- Monthly Mean Line Chart ---
    st.subheader("📊 Monthly Mean COD Levels")
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthly_mean = df.groupby("Month")["Chemical Oxygen Demand"].mean().reindex(month_order)

    st.line_chart(monthly_mean)

    # --- Feature Comparison Section ---
    st.subheader("🔍 Explore COD vs Other Features")
    st.markdown("Choose a feature to compare with COD to explore potential relationships.")

    # Let user pick a feature
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    numeric_cols.remove("Chemical Oxygen Demand")
    selected_feature = st.selectbox("Choose a feature:", numeric_cols)

    # Scatterplot of COD vs selected feature
    fig2, ax2 = plt.subplots()
    sns.scatterplot(x=selected_feature, y="Chemical Oxygen Demand", data=df, ax=ax2)
    ax2.set_title(f"COD vs {selected_feature}")
    st.pyplot(fig2)

    # Correlation coefficient
    corr = df["Chemical Oxygen Demand"].corr(df[selected_feature])
    st.markdown(f"📈 **Correlation between COD and {selected_feature}:** `{corr:.2f}`")

    # Optional tip for interpretation
    if abs(corr) > 0.6:
        st.success("✅ Strong relationship detected.")
    elif abs(corr) > 0.3:
        st.info("ℹ️ Moderate relationship.")
    else:
        st.warning("🔎 Weak or no clear linear relationship.")
