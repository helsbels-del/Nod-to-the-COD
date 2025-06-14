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
- Operational data (e.g., sludge retention time, flow rates)  
- Environmental variables (e.g., temperature, rainfall)  
- Chemical measurements (COD, TOC, NH₄, etc)  

The dataset was cleaned and preprocessed to support time-series analysis, machine learning, and interactive dashboard display.

---

## Business Requirements

1. **Understand trends in COD levels over time**  
   - Identify seasonal patterns and operational influences.  

2. **Predict future COD levels using ML models**  
   - Support proactive treatment decisions.  

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

### 2. COD Trends (EDA)

- COD by time, rainfall, season  
- Feature relationships  

### 3. Hypothesis Validation

- One expander per hypothesis  
- Plots + markdown explanations  

### 4. ML Performance

- Regression/classification results  
- Feature importances  
- Pre/post tuning comparison plots  

## Unfixed Bugs

- None at the time of writing.  
- In future, highlight known issues and limitations.  

## Deployment

### Platform: Heroku

To deploy:

1. Create app in Heroku  
2. Connect to GitHub  
3. Push main branch  
4. Open deployed link  

Use `.slugignore` to exclude large files.

## Libraries Used

Key libraries:

- `pandas` – data manipulation  
- `matplotlib`, `seaborn` – visualisation  
- `scikit-learn` – ML models  
- `joblib` – model saving  
- `streamlit` – dashboard  

## Credits

### Content

- Wikipedia (background info)  
- Tutorials from YouTube, blogs (model training)  

### Media

- Icons: Font Awesome  
- Images: Unsplash / open-source sources  

---

## Acknowledgements

Thanks to mentors, peers, and the Code Institute community for guidance and support.

### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)

* Thank the people who provided support through this project.