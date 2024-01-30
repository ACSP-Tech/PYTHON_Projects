#importing requirements
import numpy as np
import pandas as pd
#Reading the CSV url to pandas DataFrame
csv_url = "https://raw.githubusercontent.com/ACSP-Tech/PYTHON_Projects/main/adult.data.csv"
df = pd.read_csv(csv_url)

#Checking the DataFrame for na_values or typos and also taking a look at the data
print(df.info())
index = 0
column = 1
while True:
    if index < 15:
        print(df.iloc[:, index:column].value_counts())
        index += 1
        column += 1
    else:
        break

#cleaning up the data
df_cleaned = df.replace({'workclass':{'?': 'Never-worked'}, 'occupation':{'?':'unemployed'}, 'Native-country':{'?':'other'}})
print(df_cleaned.describe())
#Demographic Data Analyzer
print('\n', 'HOW MANY PEOPLE OF EACH RACE ARE IN THIS DATASET', '\n', df_cleaned['race'].value_counts())
sex = df_cleaned['sex'] == 'Male'          
print('\n', 'What is the average age of men?', '\n', df_cleaned.loc[sex, 'age'].mean())
print('\n', 'What is the percentage of people who have a Bachelor\'s degree?', '\n')
BSC_degree = df_cleaned['education'] == 'Bachelors'
percentage = (BSC_degree.sum() / len(df_cleaned)) * 100
round_num = round(percentage, 1)
print(round_num, '%')
print('\n', 'What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?', '\n')
Advanced_edu = df_cleaned['education'].isin(['Bachelors','Masters','Doctorate']) & (df_cleaned['salary'] == '>50K')
percentage = (Advanced_edu.sum() / len(df_cleaned)) * 100
round_num = round(percentage, 1)
print(round_num, '%')
print('\n', 'What is the minimum number of hours a person works per week?', '\n')
min_hours = df_cleaned['hours-per-week'] == df_cleaned['hours-per-week'].min()
print(df_cleaned.loc[min_hours, 'hours-per-week'].unique())
print('\n', 'What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?', '\n')
min_hours_salary = min_hours & (df_cleaned['salary'] == '>50K')
percentage = (min_hours_salary.sum() /min_hours.sum()) * 100
round_num = round(percentage, 1)
print(round_num, '%')
print('\n', 'What country has the highest percentage of people that earn >50K and what is that percentage?', '\n')
salary = df_cleaned['salary'] == '>50K'
country_counts = df_cleaned.loc[salary, 'native-country'].value_counts()
top_countries = country_counts[country_counts == country_counts.max()].index
percentage = country_counts.max()/country_counts.sum() * 100
print(top_countries, '\n',
      'percentage: ', percentage, '%')
print('\n', 'Identify the most popular occupation for those who earn >50K in India.', '\n')
salary = df_cleaned['salary'] == '>50K'
occupation = df_cleaned.loc[salary, 'occupation'].value_counts()
most_popular = occupation[occupation == occupation.max()].index
print(most_popular)