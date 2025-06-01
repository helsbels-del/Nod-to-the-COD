# NOD to the COD

## Project Overview

Waste water quality monitoring is an important public health concern. One of the main parameters monitored by industries using water treatment plants is the amount of COD (chemical oxygen demand). This measure the amount of oxygen required to break down organic matter in the water. High COD levels can indicate an ineffiecient treatment in the treatment process.
Nod to the COD is a data-driven project designed to support wastewater treatmewnt plants in forecasting COD levels using machine learning and data analysis techniques. The goal being to enable proactive decision making by predicting COD levels and identifying the associated factors.

## Dataset Content

Nod to the COD uses a dataset obtained from Kaggle containing operational and environmental data from a full-scale wastewater treatment plant.
The dataset includes 1,382 daily records across 19 features:

- Average outflow
- Average inflow
- energy consumption
- Ammonia
- BOD
- COD
- TN
- Average Temp
- Max Temp
- Min Temp
- Atmospheric pressure
- Average humidity
- Total rainfall
- Average visibility
- Average wind speed
- Max wind speed
- Year
- Month
- Day

These variables provide context for understanding and predicting Chemiacl Oxygen Demand (COD) levels.

## Business Requirements

### Business Requirement 1 - Understanding COD trends

Business stakeholders need insights into how COD levels fluctuate across seasons and treatmetn conditions to help support process improvements and reulatory reporting.

### Business Requirement 2 - Predict COD for operational decison making

The plant wants a predictive tool to estimate the COD levels in advance to help with chemical dosing to help reduce operational costs without comprimising the effluent quality.

## Hypothesis and how to validate?

### Hypothesis 1 (Conventional analysis)

COD levels vary significantly with seasonal factors such as rainfall and temperature.

or

Higher temperatures are associated with lower COD levels due to increased microbial activity.

- Type: Correlation hypothesis (testable using exploratory data analysis and regression)
- How to evaluate: Correlation heatmap, scatter plots, linear regression, p-value analysis
- Business Relevance: Helps operators understand seasonal variation and adapt treatmetn scedules accordingly.

### Hypothesis 2 (ML-Driven)

COD can be accurately predicted using operational and environmental data.

- Type: Predictive hypothesis (requires supervised ML)
- How to Evaluate: Train/test ML models, measure performance metrics such as R2.
- Business Relevance: Enables proactive chemicaldosing and treatment adjustments to maintain regulatory compliance.

### Hypothesis 3 (Unsupervised Learnign/Clustering)

There are distinct operational profiles or patterns in plant performance that correspond to specific COD behaviour clusters.

- Type: Exploratory hypothesis (requires unsupervised learning)
- How to Evaluate: Apply clustering (eg KMens, DBSCAN), validate using silhouette score or Davies-Bouldin Index, analyze cluster characterictics.
- Business Relevance: Allows identification of typical vs atypical plant behaviour abd supports anomoly detection and process optimisation.

## The rationale to map the business requirements to the Data Visualizations and ML tasks

Business requirement 1 - Understand COD trends
Visualisation - Time series, boxplots, heatmaps
Rationale - Identify patterns and feature relationships

Business requirement 2 - Predict COD levels
ML-Task - Regression model (Random Forest, XGBoost)
Rationale - Support proactive chemical dosing decisions.

## ML Business Case

### Predict Chemical Oxygen Demand (COD)

#### Regression Model

We want a machine learning model to predict COD levels in wastewater using historical operational and environmental data from a full-scale wastewater treatment plant.
COD is the target variable which is a continuos numerical variable, so I have considered a regression model.
The model output is a predicted COD value (mg/L) based on real-time plant measurments of other water quality parameters.

This will allow plant operators to have an advanced insight into potential high levels of COD, providing time for intervention to maintain efficeny and importantly, regulatory compliance, to avoid any fines.

#### Model Success Metrics

At least 0.75R2 score on both train and test sets

MAE (Mean Absolute Error) below 15mg/L on the test set

#### Model Failure Criteria

- If COD readings deviate by more than 50% fronm the predicted values in more than 30% of operational days over a 3 month period of use.
- R2 score consistently below 0.5 during validationa nd real-world monitoring.

### Model Output

The model outputs a single numeric value representing hte predicted COD level (in mg/L). This can be:

- Intergrated into a real-time dashboard that shows both predicted and onserved COD levels.
- Used in conjunction with operational rules to flag potential out of acceptable range values.
  
### Data Collection and Prediction

- Input Data: Readings from a data collection sensor (SCADA).
- Prediction Frequency: Daily
- Deployment - Model can be deployed via API or embedded in an interna; monitoring dashboard.

### Current Approach

Operators are currently relying on historical data and chemical dosing experiencs with no formal predictive model.
This process is reactive rather than proactive and can lead to inefficient dosing and or a breach of compliance.

### Training Data 

- Dataset includes months of operational data from a wastewater plant.
- 19 features
- Target variable - COD
- All features are numeraical data. Some data has been dropped as it is irrelevant and the time data was transformed to timestamp data.

## Predict COD Risk Level

### Classification Model

We want an ML model to classify COD readings into risk categories to help operators understand if any intervention is required. 
The target is categorical, with 3 classes:

- Low (<50 mg/l)
- Medium (50-100 mg/L)
- High (>100 mg/L)

This is a supervised, multi-class, single-label classification task.

Ideal Outcome - Operators can be alerted to high risk COD levels in real time to help improve decsion making and staying in compliance.

#### Model Success Criteria

- Recall >= 85% for High COD class on test data to avoid missing any critical alerts.
- Overall acuracy >= 75%

#### Model Failure Criteria

- If more than 25% of high COD events are missed (low recall), after 3 months of use.
- If accuracy drops below 60% in live testing over a 30 day period, leading to increased costs and overdosing.

### Model Output

A predicted class level: 'Low', 'Medium', or 'High', and the probability for each class.
Used in:

- Real-time dashboard woth traffic lights alerts
- Automated messages to suggest dosing/flow adjustments when high COD levels are predicted.

### Current Approach

No automated risk categorisation currenlty exists. Risk decisions are made after lab results or delayed sensor results interpretation.

### Training Data

- Same as regression however the target COD is discretised as using thresholds.
- Features: Pre-processed environmental and operational sensor data.

## Cluster Operational Conditions

### Clustering Model

We want to use unsupervised learning to group similar plant operating conditions that leaad to different COD behaviours.
This model will help to understand plant states and could lead to better process control.

|Ideal Outcome - Operators will gain insight into distinct operating regimes and can understand better when intervention is required, depending on the conditions.

#### Model Success Metrics

- Silhouette score >= 0.4
- Maximum 10 clusters for interpretability

#### Model Failure Criteria

- If the model produces >15 clusters, whcih are hard to explain
- Silhouette score <0.25

### Model Output

- Each record is assigned a Cluster label (e.g 0, 1, 2...)
- Output column: Operating_Cluster
- Profiles are visualised with:
  - Radar plots / parallel coordinates
  - Cluster mean values for COD, flow, ammonia, temp, etc.

### Current Approach

There is no clear understanding of recurring conditions taht lead to COD instability.
Clustering will give data-driven operating profiles

### Training Data

- Features: All scaled numeric sensor readings
- COD can be included for profiling (but not used as input)

## Dashboard Design

### Dashboard Layout Plan

#### 1. Project Summary Page

Goal : To introoduce the project, dataset, and the business requirements from the client

Content to include:

- Brief Description of the wastewater treatmetn context.
- Dataset overview (number of rows, key features)
- Summary of Business Requirements
  - Undestand patterns influencing COD levles.
  - Predict COD levels for smarter dosing predictions

Optional Visual elements:

- Summary cards; e.g COD avg: xx mg?L, Total days:  1382, etc.
- Pie Chart or bar chart of feature types (eg. environmental vs operational)

#### 2. Data Analytics and ML Pages

Goal: To show how I have addressed each of the business requirements using analysis and ML.

A. Conventional Data Analysis

- Correltation heatmap showing relationship between features and COD.
- Line chart of COD over time.
- Boxplots of COD by month or season
- Rainfall vs COD scatter plot.

B. Machine Learning

- Feature importance bar plot (eg. from Random Forest)
- Actual vs Predicted COD plot.
- Summary table of key metrics: MAE, RMSE, R2.
  
#### 3. Hypothesis Validation Page

Goal: To clearly communicate the hypothesis and how they were tested.

Structure:

- State Hypotheses:
  - COD is influenced by seasonla factors.
  - COD can be predicted using operational and environmental features.
- Visualisations used to test each (refer to analysis inssction 2)
- Summarise findings:
  - "We observed strong correlation between COD and X, supporting Hypothesis 1."
  - "The model achieved R2 of X, supporting Hypothesis 2."

#### 4. Technical ML Pipeline Page

Goal: To showcase the technical implementation, especially if you deployed an ML model.

Include:

- Diagram of the ML pipeline (eg. Data Cleaning + feature Selection + Scaling + Model training + Evaluation)
- Description of each pipeline step:
  - How you handled missing data, encoded time etc
  - Which models you used and why
  - Hyperparameter tunig approach
- Model performance metrics with charts and tables
- Deployment notes: how and where the model could be used.

Optional bonus: Show a simplified flowchart or Sankey diagram of the pipeline.

# EPICS and User Stories

### Epic 1: Data Preparation

- User Story 1.1: As a data scientist, I want to clean and format the sataset so I can analyse any trends and build models.
- User Story 1.2: As a data scientist, I want to enginerr a date feature to analyse seasonal patterns.

### Epic 2: Data Analysis

- User Story 2.1: As a stakeholder, I want to see what environmental and operational variables influence COD so I can understand drivers of poor water quality.
  
### Epic 3: Machine Learning

- User Story 3.1: As a data scientist, i want to train regression models to predict COD based on past data.
- User Story 3.2: As a stakeholder, I want to evaluate model performance so that I can trust the predictions.

### Epic 4: Visualisation and Reporting

- Use Story 4.1: As as takeholder, I want a dashboard to explore COD trends and model predictions interactively.




## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
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

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people who provided support through this project.

