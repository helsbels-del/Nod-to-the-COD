import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def page_eda_cod_trends_body():
    st.title("📈 COD Levels by Month")
    
    df = pd.read_csv("outputs/datasets/collection/Data-Melbourns_F_fixed.csv", parse_dates=["date"])
    df["Month"] = df["date"].dt.strftime("%b")
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)

    fig, ax = plt.subplots(figsize=(10, 5))
    df.boxplot(column="Chemical Oxygen Demand", by="Month", ax=ax)
    plt.title("COD Levels by Month")
    plt.suptitle("")
    plt.xlabel("Month")
    plt.ylabel("COD (mg/L)")
    st.pyplot(fig)
