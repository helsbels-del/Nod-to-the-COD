import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def page_cod_analysis_body():
    st.title("🧪 COD Analysis Explorer")

    st.markdown("""
    Use the dropdown below to explore different aspects of COD in the treatment process.
    Each option reveals a different visual insight or trend.
    """)

    # Load data
    df = pd.read_csv("outputs/datasets/collection/Data-Melbourns_F_fixed.csv", parse_dates=["date"])
    df["Month"] = df["date"].dt.strftime("%b")
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)

    # Dropdown menu
    analysis_option = st.selectbox(
        "Select an analysis to view:",
        (
            "COD Distribution",
            "Monthly COD Levels",
            "Correlation Heatmap",
            "Scatter: BOD vs COD"
        )
    )

    # === Display based on selection ===

    if analysis_option == "COD Distribution":
        st.subheader("📊 COD Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df["Chemical Oxygen Demand"], bins=30, kde=True, ax=ax)
        st.pyplot(fig)

    elif analysis_option == "Monthly COD Levels":
        st.subheader("📈 COD by Month")
        fig, ax = plt.subplots(figsize=(10, 5))
        df.boxplot(column="Chemical Oxygen Demand", by="Month", ax=ax)
        plt.title("COD by Month")
        plt.suptitle("")
        plt.xlabel("Month")
        plt.ylabel("COD (mg/L)")
        st.pyplot(fig)

    elif analysis_option == "Correlation Heatmap":
        st.subheader("🔍 Variable Correlations with COD")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    elif analysis_option == "Scatter: BOD vs COD":
        st.subheader("⚖️ BOD vs COD")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x="Biological Oxygen Demand", y="Chemical Oxygen Demand", ax=ax)
        st.pyplot(fig)
