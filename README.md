# NOD to the COD

## Summary

**Nod to the COD** is a machine learning project designed to help wastewater treatment plants predict and manage Chemical Oxygen Demand (COD) levels using environmental and operational data. By combining conventional analysis with supervised and unsupervised ML, the app empowers operators to optimise processes, reduce costs, and stay compliant.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Hypotheses and Validation Strategies](#hypotheses-and-validation-strategies)
- [ML Business Case](#ml-business-case)
- [Dashboard Design](#dashboard-design)
- [Epics and User Stories](#epics-and-user-stories)
- [Unfixed Bugs](#unfixed-bugs)
- [Testing](#testing)
- [Deployment](#deployment)
- [Libraries Used](#libraries-used)
- [Credits](#credits)

---

## Project Overview

This data science project investigates trends and predictions of Chemical Oxygen Demand (COD) in wastewater treatment using machine learning. The goal is to support sustainable water management through actionable insights and predictive tools.

The project includes:

- Exploratory Data Analysis (EDA) on COD trends and influencing factors  
- Hypothesis testing around operational and environmental drivers of COD  
- Regression and classification models for COD prediction  
- A multi-page interactive dashboard for exploration and prediction  

---

## Dataset Content

The dataset was collected from a full-scale wastewater treatment plant and includes:

- Temporal data (month, season)  
- Operational data (e.g., flow rates)  
- Environmental variables (e.g., temperature, rainfall)  
- Chemical measurements (COD, TOC, NH₄, etc)  

The dataset was cleaned and preprocessed to support time-series analysis, machine learning, and interactive dashboard display.

---

## Business Requirements

1. **Understand trends in COD levels over time**  
   - Identify seasonal patterns and operational influences.
   - Business stakeholders need insights into how COD levels fluctuate across seasons and treatment conditions to help support process improvements and regulatory reporting.

2. **Predict future COD levels using ML models**  
   - Support proactive treatment decisions.  
   -The plant wants a predictive tool to estimate the COD levels in advance to help with chemical dosing to help reduce operational costs without compromising the effluent quality.

3. **Test specific hypotheses related to operational/environmental drivers**  
   - Validate assumptions with data-backed insights.  

---

## Hypotheses and Validation Strategies

### Hypothesis 1 – Conventional Analysis

**Higher temperatures are associated with lower COD levels due to increased microbial activity.**

- **Type:** Correlation hypothesis  
- **Validation:** Correlation heatmap, scatter plots, linear regression, p-value  
- **Business Impact:** Understanding seasonal variation supports adaptive treatment planning  

### Hypothesis 2 – ML-Driven

**COD can be accurately predicted using operational and environmental data.**

- **Type:** Predictive (supervised ML)  
- **Validation:** Train/test ML models, evaluate using R², MAE, RMSE  
- **Business Impact:** Enables proactive chemical dosing and better compliance  

### Hypothesis 3 – Unsupervised Learning  

**Distinct operational profiles exist that correspond to specific COD behaviour.**  

- **Type:** Exploratory (unsupervised learning)  
- **Validation:** Clustering (e.g., KMeans), silhouette score, Davies-Bouldin Index  
- **Business Impact:** Identifies atypical plant behaviour for anomaly detection and process optimisation  

---

## Mapping Business Requirements to ML and Visualisation

| Business Requirement | Visualisation or ML Task              | Rationale                                           |
|----------------------|----------------------------------------|-----------------------------------------------------|
| COD trends           | Time series, boxplots, heatmaps       | Understand seasonal and operational influences      |
| Predict COD levels   | Regression/classification models      | Enable proactive and optimised decision-making      |
| Test hypotheses      | Correlation plots, clustering, ML     | Support with data-driven validation and insight     |

---

## ML Business Case

### Predicting Chemical Oxygen Demand (Regression)

**Objective:** Predict COD levels based on operational and environmental data.  
**Model:** Random Forest Regressor  
**Target Variable:** COD (continuous, mg/L)  
**Success Criteria:**  

- R² ≥ 0.75  
- MAE ≤ 15 mg/L  

**Failure Criteria:**

- R² < 0.5 consistently  
- >30% of days deviate by >50% from predicted  

**Output:**

- Numeric COD prediction  
- Displayed in a dashboard alongside observed values  

**Current Workflow:**

Operators rely on historical knowledge. This is reactive and may lead to overdosing or non-compliance.

---

### Classifying COD Risk Level (Classification)

**Objective:** Classify COD into risk categories  
**Model:** Random Forest Classifier  
**Classes:**

- Low (<50 mg/L)  
- Medium (50–100 mg/L)  
- High (>100 mg/L)  

**Success Criteria:**

- Recall ≥ 85% for “High” COD class  
- Overall accuracy ≥ 75%  

**Failure Criteria:**

- Recall < 75% for “High” COD after 3 months  
- Accuracy < 60% over 30 days  

**Output:**

- Class label + probability  
- Dashboard alert system  

---

### Clustering Operational Conditions (Unsupervised)

**Objective:** Identify common operating patterns influencing COD  
**Model:** KMeans or DBSCAN  
**Success Criteria:**

- Silhouette score ≥ 0.4  
- ≤ 10 clusters for interpretability  

**Failure Criteria:**

- >15 indistinct clusters  
- Silhouette score < 0.25  

**Output:**

- Cluster label  
- Visualised via radar plots or cluster summaries  

---

## Dashboard Design

### 1. Project Summary Page

- Project intro  
- Dataset overview  
- Key metrics  

### 2. COD Trends and Analysis

- COD by time, rainfall, season  
- Feature relationships  

### 3. Predict COD

- User can enter values for 3 variables to predict the COD

### 4. Project Hypotheses

- One expander per hypothesis  
- Plots + markdown explanations  

# EPICS and User Stories

### Epic 1: Data Preparation

- User Story 1.1: As a data scientist, I want to clean and format the dataset so I can analyse any trends and build models.
  
  This is addressed in the Data Cleaning notebook where the data has been sorted and cleaned for analysis.
- User Story 1.2: As a data scientist, I want to engineer a date feature to analyse seasonal patterns.

  This is addressed in the Data cleaning notebook and the eda_cod_trends notebooks, creating Month and Month_Parsed features for time trend analysis.

### Epic 2: Data Analysis

- User Story 2.1: As a stakeholder, I want to see what environmental and operational variables influence COD so I can understand drivers of poor water quality.

  This is addressed in eda_cod_trends notebook via correlation analysis and scatter plots.
  
### Epic 3: Machine Learning

- User Story 3.1: As a data scientist, i want to train regression models to predict COD based on past data.

  This is addressed in COD_Model_Development and model_tuning_and_comparison notebooks with Random Forest regression pipeline and tuning.
- User Story 3.2: As a stakeholder, I want to evaluate model performance so that I can trust the predictions.

  This is addressed in model_tuning_and_comparison notebook with MAE, RMSE, R² comparison plots. They can then make real time COD predictions on the Streamlit App

### Epic 4: Visualisation and Reporting

- Use Story 4.1: As as takeholder, I want a dashboard to explore COD trends and model predictions interactively.

  This is addressed with the Steamlit dashboard which can be used to model predictions using selected features.

## Unfixed Bugs

There were no unfixed bugs at the time of submission of my project.

## Testing

All the .py files were run through the CI Python Linter and all pages were clear with no errors at the time of submitting my project.
All streamlit app pages were checked to make sure the tick boxes loaded the relevant plots and information.

## Deployment

### Platform: Heroku

### Heroku

- The App live link is: [Live App Link](https://nod-to-the-cod-5d011c7c047b.herokuapp.com/))
- Set the runtime.txt Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. I logged in to Heroku and created an app.
2. In the Deploy tab, I connected to GitHub and selected the repository helsbels-del/Nod-to-the-COD and clicked connect.
3. I then deplyed the main branch.
4. Once the deployment process had completed, I click on the view tab and the app opens with no issues.

## Libraries Used

Key libraries:

- `pandas` – data manipulation  
- `matplotlib`, `seaborn` – visualisation  
- `scikit-learn` – ML models  
- `joblib` – model saving  
- `streamlit` – dashboard  

## Credits

### Content

- Information gained from the code institute predictive analytics coursework.
- Wikipedia (background info)  
- w3schools website
- Icons: Unicode emojis generated by ChatGPT where used to enchance the verall look of my project  

---

## Acknowledgements

Thanks to my mentor Mo Shami for all his help and guidance and also to the Code Institute community and freinds and family for helping me to keep going.
