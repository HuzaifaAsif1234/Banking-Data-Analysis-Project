📊 ## Exploratory Data Analysis (EDA) on Banking Dataset using Python
📌 Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on a banking customer dataset using Python in a Jupyter Notebook. The goal is to understand customer financial behavior, identify patterns, and extract meaningful insights through data cleaning, visualization, and statistical analysis.

The project demonstrates an end-to-end data analysis workflow, starting from data loading and preprocessing to visualization and correlation analysis.

🎯 ## Objective

- Understand the structure and quality of the dataset

- Perform data cleaning and preprocessing

- Analyze categorical and numerical features

- Identify patterns and relationships between financial variables

- Generate insights that can support business and analytical decisions

🗂 ## Dataset Description

- Source: CSV file (Banking Dataset)

- Type: Structured tabular data

- Domain: Banking / Finance

- Features include:

- Estimated Income

- Superannuation Savings

- Credit Card Balance

- Banking Accounts

- Saving Accounts

- Foreign Currency Accounts

- Customer demographic and categorical attributes

🛠 ## Tools & Technologies

- Python

- Pandas – data manipulation and analysis

- NumPy – numerical operations

- Matplotlib & Seaborn – data visualization

- MySQL Connector – database connectivity

- Jupyter Notebook

🔍 ## EDA Workflow
1️⃣ # Data Loading

Loaded CSV data into a Pandas DataFrame

Connected Python with a MySQL database to demonstrate database integration

2️⃣ # Initial Data Exploration

- Used .head(), .tail(), .shape(), and .info() to understand:

- Dataset size

- Data types

- Missing values

3️⃣ # Data Cleaning

Removed unnecessary and index-like columns

Checked and validated missing values to ensure data quality

4️⃣ # Categorical Feature Analysis

- Identified categorical columns dynamically

- Used count plots to visualize category distributions

- Helped detect class imbalance and dominant categories

![Univariate Data of BrId in Categories](<img width="395" height="263" alt="Brid univariate categorical data" src="https://github.com/user-attachments/assets/c07d09c9-5690-4a58-b443-62419487d8a2" />
)
![Univariate Data of BrId in Categories](<img width="395" height="262" alt="genderid univariate cat data" src="https://github.com/user-attachments/assets/addb8759-0a5c-461c-ac5f-f748d5097a0f" />
)
![Bivariate Data of Amount of Credit cards in Categories](<img width="395" height="263" alt="amtOfCC bivariate cat data" src="https://github.com/user-attachments/assets/a8fa7d0c-dd50-4fb7-ac69-ffd4966a9de1" />
)
![Bivariate Data of Nationality in Categories](<img width="389" height="262" alt="nationality bivariate cat data" src="https://github.com/user-attachments/assets/ba539d85-fad1-4b57-9942-03e7229a1a66" />
)
![Categorical data analysis using Loyalty Classification](<img width="507" height="278" alt="Loyalty Classification" src="https://github.com/user-attachments/assets/decbbc7a-0181-4288-8ce0-7da9a4bffa8f" />
)
![Categorical data analysis using Income Band](<img width="507" height="278" alt="Income Band" src="https://github.com/user-attachments/assets/4b9cf595-eeee-4f45-97a0-86deb8ba8c6d" />
)


5️⃣ # Numerical Feature Analysis

- Analyzed distributions using histograms and KDE plots

- Studied skewness and spread of financial variables

![Numerical data analysis using estimated inome](<img width="1728" height="1065" alt="estimated income" src="https://github.com/user-attachments/assets/809ec68b-c097-41e8-942b-dbff4c136cfa" />
)
![Numerical data analysis using superannuation savings](<img width="1728" height="1065" alt="superannuation savings" src="https://github.com/user-attachments/assets/39ff25b2-f20f-49e0-bebd-5bf0f4f8d3b5" />
)

6️⃣ # Correlation Analysis

- Generated a correlation matrix for numerical features

- Visualized relationships using a heatmap

- Identified strong and weak correlations for better feature understanding

![Correlation Heatmaps](<img width="774" height="806" alt="correlation Heatmap" src="https://github.com/user-attachments/assets/75b73dcb-dad1-42af-b7dd-93991319a066" />
)

📈 ## Key Insights

- Income and savings-related features show varied distributions across customers

- Certain financial attributes exhibit moderate correlation, indicating potential behavioral patterns like checking accounts and Bank deposits.

- Visual analysis helps in identifying outliers and skewed distributions

🧠 ## Skills Demonstrated

- Exploratory Data Analysis (EDA)

- Data Cleaning & Preprocessing

- Data Visualization & Storytelling

- Python for Data Analysis

- SQL & Database Integration

- Analytical Thinking with Business Context

🚀 Future Improvements

- Feature engineering for predictive modeling

- Handling outliers and skewness more rigorously

- Applying machine learning models for customer segmentation

- Deeper business-driven insights and recommendations

📬 ## Contact

If you find this project interesting or have suggestions, feel free to connect with me on LinkedIn.
