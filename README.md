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

<img src=<img width="508" height="323" alt="Brid univ cat" src="https://github.com/user-attachments/assets/654f6d1a-bd67-4e2f-acd2-2ed508a58869" />
<img src=<img width="576" height="337" alt="genId univ cat" src="https://github.com/user-attachments/assets/e6adb1b6-aa1d-4946-9fc3-4bd079028750" />
<img src=<img width="606" height="355" alt="amtOf cc bivar" src="https://github.com/user-attachments/assets/8ea4b525-f299-4ae0-b8e2-82e26241ee91" />
<img src=<img width="559" height="335" alt="Nationality bivar" src="https://github.com/user-attachments/assets/65f62d92-ad5a-4160-84fa-7ca4a473aece" />
<img src=<img width="702" height="326" alt="Loyalty" src="https://github.com/user-attachments/assets/69ea7906-7f7a-4133-8b6c-cfecdffef490" />
<img src=<img width="660" height="327" alt="Income Band" src="https://github.com/user-attachments/assets/630d1dcd-e091-402e-80d9-85ca4663378d" />

### 5️⃣ Numerical Feature Analysis

- Analyzed distributions using histograms and KDE plots  
- Studied skewness and spread of financial variables  

#### Sample Visualizations

<img src=<<img width="447" height="253" alt="Estim inc" src="https://github.com/user-attachments/assets/1dd0e836-4dd7-403d-b968-f75c94f34922" />
<img src=<img width="397" height="262" alt="super annu" src="https://github.com/user-attachments/assets/a041dfc1-a281-40aa-b771-3804bc87b918" />

### 6️⃣ Correlation Analysis

- Generated a correlation matrix for numerical features  
- Visualized relationships using a heatmap  
- Identified strong and weak correlations for better feature understanding  

#### Correlation Heatmap

<img src="<img width="845" height="761" alt="Heatmap" src="https://github.com/user-attachments/assets/c46b5caf-a084-40b1-a169-65f4ce42cef7" />


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
