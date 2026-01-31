Exploratory Data Analysis of Banking Dataset using Python

Demonstrates connecting Python (Jupyter Notebook) to a MySQL database for EDA

Creates a MySQL database named test by connecting to a local MySQL server using Python.

=================================================================================================================================================
import mysql.connector as connection

try:
    mydb = connection.connect(host = 'localhost',user='root',passwd='Huzaifaasif231',use_pure= True)
    
    query = 'Create Database test'
    
    cursor = mydb.cursor()
    cursor.execute(query)
    print(cursor.fetchall())
except Exception as e:
    mydb.close()
    print(str(e))

=================================================================================================================================================
Importing libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import numpy as np

==================================================================================================================================================
Income Band


bins = [0,100000,300000,float('inf')]
labels =['Low','Med','High']
df['Income band'] = pd.cut(df['Estimated Income'], bins = bins, labels= labels, right= False)

----------------------------------------------------------------------------------------------------------
Table of Income Band:
df['Income band'].value_counts()

-----------------------------------------------------------------------------------------------------------
Bar Chart of Income Band:
df['Income band'].value_counts().plot(kind = 'bar')

==================================================================================================================================================================================================
Examine the distribution of unique categories in unique categorical coloumns:
categorical_cols = df[["BRId","GenderId","IAId","Amount of Credit Cards","Nationality", 'Occupation','Fee Structure','Loyalty Classification','Properties Owned','Risk Weighting','Income band']].columns
for col in categorical_cols:
    print(f"Value counts for '{col}': ")
    display(df[col].value_counts())

------------------------------------------------------------------------------------------------------------
Univariate Categorical Analysis:

for i, predictor in enumerate(df[["BRId","GenderId","IAId","Amount of Credit Cards","Nationality", 'Occupation','Fee Structure','Loyalty Classification','Properties Owned','Risk Weighting','Income band']].columns):
    plt.figure(i)
    sn.countplot(data = df, x = predictor)

------------------------------------------------------------------------------------------------------------
Bivariate Categorical Analysis:
for i, predictor in enumerate(df[["BRId","GenderId","IAId","Amount of Credit Cards","Nationality", 'Occupation','Fee Structure','Loyalty Classification','Properties Owned','Risk Weighting','Income band']].columns):
    plt.figure(i)
    sn.countplot(data = df, x = predictor, hue = 'GenderId')

========================================================================================================================================================================================================
Numerical Analysis:

numerical_cols = ['Estimated Income', 'Superannuation Savings','Credit Card Balance','Bank Loans','Bank Deposits','Checking Accounts','Saving Accounts','Foreign Currency Account']
plt.figure(figsize = (30,25))
for i, col in enumerate(numerical_cols):
    plt.subplot(4,3,i+1)
    sn.histplot(df[col],kde = True)
    plt.title(col)
plt.show()

==========================================================================================================================================================================================================

Heatmap:

numerical_cols = ['Estimated Income', 'Superannuation Savings','Credit Card Balance','Bank Loans','Bank Deposits','Checking Accounts','Saving Accounts','Foreign Currency Account']
correlation_matrix = df[numerical_cols].corr()
plt.figure(figsize=(12,12))
sn.heatmap(correlation_matrix, annot = True, cmap = 'crest', fmt = '.2f')



