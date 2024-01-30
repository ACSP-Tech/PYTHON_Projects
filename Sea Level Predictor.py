import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#importing the data
csv_url = 'https://raw.githubusercontent.com/ACSP-Tech/PYTHON_Projects/main/epa-sea-level.csv'
df = pd.read_csv(csv_url, parse_dates=['Year'])
#displaying only the year in the year column
df['Year'] = df['Year'].dt.year
#taking a quick look and understanding the data
print(df.head())
print(df.info())
print(df.describe())
#1.Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis. 
sns.relplot(x='Year', y='CSIRO Adjusted Sea Level', data=df, kind='scatter' )
plt.title('Rise in Sea Level')
#2. Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
from scipy.stats import linregress
sns.relplot(x='Year', y='CSIRO Adjusted Sea Level', data=df, kind='scatter' )
# Using linregress to calculate the slope and intercept
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
# Creating an array of years for the line of best fit
years_for_fit = range(df['Year'].min(), 2051)
# Calculating the corresponding sea levels using the linear regression equation
sea_levels_for_fit = [slope * year + intercept for year in years_for_fit]
# Plot the line of best fit
plt.plot(years_for_fit, sea_levels_for_fit, color='red', label='Line of Best Fit')
# Set the legend
plt.legend()
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.grid(True)
plt.show()
#3. Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
Adjusted_year = df['Year'][df['Year'] >= 2000]
Adjusted_CSIRO_Adjusted_Sea_Level = df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000]
sns.relplot(x=Adjusted_year, y=Adjusted_CSIRO_Adjusted_Sea_Level, kind='scatter' )
# Using linregress to calculate the slope and intercept
slope, intercept, r_value, p_value, std_err = linregress(Adjusted_year , Adjusted_CSIRO_Adjusted_Sea_Level)
# Creating an array of years for the line of best fit
years_for_fit = range(Adjusted_year.min(), 2051)
# Calculating the corresponding sea levels using the linear regression equation
sea_levels_for_fit = [slope * year + intercept for year in years_for_fit]
# Plot the line of best fit
plt.plot(years_for_fit, sea_levels_for_fit, color='red', label='Line of Best Fit')
# Set the legend
plt.legend()
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.grid(True)
plt.show()