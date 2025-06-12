import streamlit as st
from app_pages.multipage import MultiPage

# Import your pages
from app_pages.page_summary import page_summary_body
from app_pages.page_predict import page_predict_body
from app_pages.page_cod_analysis import page_cod_analysis_body
from app_pages.page_cod_hypotheses import page_cod_hypotheses_body
from app_pages.page_eda_cod_trends import page_cod_trends_body

app = MultiPage(app_name="Nod to the COD")

# Register pages
app.add_page("Project Summary", page_summary_body)
app.add_page("Predict COD", page_predict_body)
app.add_page("COD Analysis Explorer", page_cod_analysis_body)
app.add_page("Project Hypotheses", page_cod_hypotheses_body)
app.add_page("COD Trends (EDA)", page_cod_trends_body)

# Run the app
app.run()

