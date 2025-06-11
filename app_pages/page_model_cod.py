import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

def page_model_cod_body():
    st.title("🧠 COD Model Insights")

    model = joblib.load("outputs/models/final_model.pkl")

    importances = model.feature_importances_
    features = model.feature_names_in_

    feat_df = pd.DataFrame({"Feature": features, "Importance": importances})
    feat_df = feat_df.sort_values(by="Importance", ascending=True)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(feat_df["Feature"], feat_df["Importance"])
    ax.set_title("Feature Importances (COD Prediction)")
    st.pyplot(fig)
