# 📊 Exploratory Data Analysis (EDA) on Banking Dataset using Python

## 📌 Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on a banking customer dataset using Python in a Jupyter Notebook. The goal is to understand customer financial behavior, identify patterns, and extract meaningful insights through data cleaning, visualization, and statistical analysis.

The project demonstrates an end-to-end data analysis workflow, starting from data loading and preprocessing to visualization and correlation analysis.

## 🎯 Objective

- Understand the structure and quality of the dataset  
- Perform data cleaning and preprocessing  
- Analyze categorical and numerical features  
- Identify patterns and relationships between financial variables  
- Generate insights that can support business and analytical decisions  

## 🗂 Dataset Description

- **Source:** CSV file (Banking Dataset)  
- **Type:** Structured tabular data  
- **Domain:** Banking / Finance  
- **Features include:**  
  - Estimated Income  
  - Superannuation Savings  
  - Credit Card Balance  
  - Banking Accounts  
  - Saving Accounts  
  - Foreign Currency Accounts  
  - Customer demographic and categorical attributes  

## 🛠 Tools & Technologies

- Python  
- Pandas – data manipulation and analysis  
- NumPy – numerical operations  
- Matplotlib & Seaborn – data visualization  
- MySQL Connector – database connectivity  
- Jupyter Notebook  

## 🔍 EDA Workflow

### 1️⃣ Data Loading

- Loaded CSV data into a Pandas DataFrame  
- Connected Python with a MySQL database to demonstrate database integration  

### 2️⃣ Initial Data Exploration

- Used `.head()`, `.tail()`, `.shape()`, and `.info()` to understand:  
  - Dataset size  
  - Data types  
  - Missing values  

### 3️⃣ Data Cleaning

- Removed unnecessary and index-like columns  
- Checked and validated missing values to ensure data quality  

### 4️⃣ Categorical Feature Analysis

- Identified categorical columns dynamically  
- Used count plots to visualize category distributions  
- Helped detect class imbalance and dominant categories  

#### Sample Visualizations

<img src="eda_images/Brid_univariate_categorical_data.png" alt="Brid univariate categorical data" width="900" height="600"/>
<img src="eda_images/GenderID_univariate_categorical_data.png" alt="Gender ID univariate categorical data" width="900" height="600"/>
<img src="eda_images/AmtOfCC_bivariate_categorical_data.png" alt="AmtOfCC bivariate categorical data" width="900" height="600"/>
<img src="eda_images/Nationality_bivariate_categorical_data.png" alt="Nationality bivariate categorical data" width="900" height="600"/>
<img src="eda_images/Loyalty_Classification.png" alt="Loyalty Classification" width="900" height="600"/>
<img src="eda_images/Income_Band.png" alt="Income Band" width="900" height="600"/>

### 5️⃣ Numerical Feature Analysis

- Analyzed distributions using histograms and KDE plots  
- Studied skewness and spread of financial variables  

#### Sample Visualizations

<img src="eda_images/Estimated_Income.png" alt="Estimated Income" width="1000" height="700"/>
<img src="eda_images/Superannuation_Savings.png" alt="Superannuation Savings" width="1000" height="700"/>

### 6️⃣ Correlation Analysis

- Generated a correlation matrix for numerical features  
- Visualized relationships using a heatmap  
- Identified strong and weak correlations for better feature understanding  

#### Correlation Heatmap

<img src="<img width="845" height="761" alt="Heatmap" src="https://github.com/user-attachments/assets/c46b5caf-a084-40b1-a169-65f4ce42cef7" />
" alt="Correlation Heatmap" width="1000" height="700"/>

## 📈 Key Insights

- Income and savings-related features show varied distributions across customers  
- Certain financial attributes exhibit moderate correlation, indicating potential behavioral patterns like checking accounts and bank deposits  
- Visual analysis helps in identifying outliers and skewed distributions  

## 🧠 Skills Demonstrated

- Exploratory Data Analysis (EDA)  
- Data Cleaning & Preprocessing  
- Data Visualization & Storytelling  
- Python for Data Analysis  
- SQL & Database Integration  
- Analytical Thinking with Business Context  

## 🚀 Future Improvements

- Feature engineering for predictive modeling  
- Handling outliers and skewness more rigorously  
- Applying machine learning models for customer segmentation  
- Deeper business-driven insights and recommendations  

## 📬 Contact

If you find this project interesting or have suggestions, feel free to connect with me on LinkedIn.
