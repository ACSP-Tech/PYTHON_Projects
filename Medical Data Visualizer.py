import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Import data
csv_url = "https://raw.githubusercontent.com/ACSP-Tech/PYTHON_Projects/main/medical_examination.csv"
df = pd.read_csv(csv_url)
#Checking the DataFrame for na_values or typos and also taking a look at the data
print(df.info(), '\n', df.describe())
#cleaning up the data
df_clean = df.copy()
# Age: Considering leap years, rounding up the result to whole number, changing the dtype to int, changing the values of the age column, checking for invalid data or missing value in the age column
print('\n\n')
#Data Vizulaization - age(before cleaning)
sns.displot(df_clean['age'], rug=True, kde=True)
plt.title('age distribution')
plt.show()
#cleaning the age column
df_clean['age']= round(df_clean['age'] / 365.25).astype(int)
print('\n\n')
#Data Vizulaization - age(after cleaning)
sns.displot(df_clean['age'], rug=True, kde=True)
plt.title('age distribution after cleaning')
plt.show()
#height:creating an interquantile range(iqr), using the iqr to obtain the upper_limit and lower_limit and droping the outliers
print('\n\n')
#Data Vizulaization - height(before cleaning
sns.displot(df_clean['height'], rug=True, kde=True)
plt.title('height distribution')
plt.show()
#cleaning the height column
iqr = df_clean['height'].quantile(0.75) - df_clean['height'].quantile(0.25)
upper_limit =  df_clean['height'].mean() + 2 * iqr
lower_limit =  df_clean['height'].mean() - 2 * iqr
df_clean = df_clean[(df_clean['height'] <= upper_limit) & (df_clean['height'] >= lower_limit)]
print('\n\n')
#Data Vizulaization - height(after cleaning)
sns.displot(df_clean['height'], rug=True, kde=True)
plt.title('height distribution after cleaning')
plt.show()
#weight:creating an interquantile range(iqr), using the iqr to obtain the upper_limit and lower_limit and droping the outliers
print('\n\n')
#Data Vizulaization - weight(before cleaning)
sns.displot(df_clean['weight'], rug=True, kde=True)
plt.title('weight distribution')
plt.show()
#cleaning the weight column
iqr = df_clean['weight'].quantile(0.75) - df_clean['weight'].quantile(0.25)
upper_limit =  df_clean['weight'].mean() + 2 * iqr
lower_limit =  df_clean['weight'].mean() - 2 * iqr
df_clean = df_clean[(df_clean['weight'] <= upper_limit) & (df_clean['weight'] >= lower_limit)]
print('\n\n')
#Data Vizulaization - weight(after cleaning)
sns.displot(df_clean['weight'], rug=True, kde=True)
plt.title('weight distribution after cleaning')
plt.show()
#ap_hi and ap_lo, dropping invalid data where ap_lo is greater than ap_hi:
print('\n\n')
#Data Vizulaization - ap_hi and ap_lo(before cleaning)
df_clean[['ap_hi', 'ap_lo']].plot(figsize=(12,6), title='ap_hi and ap_lo distribution')
for index, row in df_clean[['ap_hi', 'ap_lo']].iterrows():
    ap_hi_value = row['ap_hi']
    ap_lo_value = row['ap_lo']
    condition = ap_lo_value > ap_hi_value
    if condition:
       df_clean.drop(index, inplace=True)
#Data Vizulaization - ap_hi and ap_lo(after cleaning)
df_clean[['ap_hi', 'ap_lo']].plot(figsize=(12,6), title='ap_hi and ap_lo distribution after cleaning')
# Resetting index after dropping rows
df_clean.reset_index(drop=True, inplace=True)
#Gluc and cholesterol: Normalize the data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1,make the value 0. If the value is more than 1, make the value 1.:
print('\n\n')
#Data Vizulaization - gluc and cholesterol (before cleaning)
print(df_clean['cholesterol'].value_counts())
print(df_clean['gluc'].value_counts())
for index, row in df_clean[['cholesterol', 'gluc']].iterrows():
    cholesterol_value = row['cholesterol']
    gluc_value = row['gluc']
    if cholesterol_value > 1:
        df_clean.at[index, 'cholesterol'] = 1
    elif cholesterol_value == 1:
        df_clean.at[index, 'cholesterol'] = 0
    if gluc_value > 1: 
        df_clean.at[index, 'gluc'] = 1
    elif gluc_value == 1:
        df_clean.at[index, 'gluc'] = 0
#Data Vizulaization - gluc and cholesterol (after cleaning)
print(df_clean['cholesterol'].value_counts())
print(df_clean['gluc'].value_counts())
#overweight:Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
df_clean['height'] = df_clean['height']/100 #converting the height column to meters
BMI = df_clean['weight']/(df_clean['height']**2)
df_clean['overweight'] = BMI
print(df_clean['overweight'].head()) #data vizualizuation: checking the overweight before assigning zero and ones
for index, row in df_clean.iterrows():
    BMI = row['overweight']
    if BMI > 25:
        df_clean.at[index, 'overweight'] = 1
    else:
        df_clean.at[index, 'overweight'] = 0
df_clean['overweight'] = df_clean['overweight'].astype(int)
print(df_clean['overweight'].head()) #data vizualizuation: checking the overweight after assigning zero and ones
#DATA ANAlYSIS
#1. Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). The dataset should be split by 'Cardio' so there is one chart for each cardio value. 
df_long = pd.melt(df_clean[['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke', 'cardio']], 
                  id_vars= ['cardio'], 
                  var_name='Variable', 
                  value_name='Value')
sns.catplot(x='Variable', 
            hue='Value', 
            col='cardio', 
            col_wrap=2,  # Number of columns in the grid
            kind='count',  # Use 'count' for value counts
            data=df_long,
            height=4, aspect=1.2,
            legend=True)
plt.show()
#2. Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's heatmap(). Mask the upper triangle. 
correlation_matrix = df_clean.corr() 
mask = np.triu(correlation_matrix)
sns.heatmap(correlation_matrix, annot=True, mask=mask, fmt=".1f", square=True, vmin=-0.08, vmax=0.25)
plt.show()