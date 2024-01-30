import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Import data: import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
csv_url = "https://raw.githubusercontent.com/ACSP-Tech/PYTHON_Projects/main/fcc-forum-pageviews.csv"
df = pd.read_csv(csv_url, parse_dates=['date'])
print(df.head())
#Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
#cleaning up the data
df_clean = df
iqr = df_clean['value'].quantile(0.75) - df_clean['value'].quantile(0.25)
upper_limit =  df_clean['value'].mean() + 2 * iqr
lower_limit =  df_clean['value'].mean() - 2 * iqr
df_clean = df_clean[(df_clean['value'] <= upper_limit) & (df_clean['value'] >= lower_limit)]
#Data Analysis
#1- Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.
def draw_line_plot(x, y, values):
    plt.figure(figsize=(16,9))
    sns.lineplot(x=x, y=y, data=values, color='darkred');
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()
draw_line_plot('date', 'value', df_clean)
print('\n\n\n')
#2. Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.
def draw_bar_plot(values):
    values_copy = values.copy()
    values_copy['year'] = values_copy['date'].dt.year
    values_copy['months'] = values_copy['date'].dt.month_name()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    values_copy['months'] = pd.Categorical(values_copy['months'], categories=month_order, ordered=True)
    df_grouped = values_copy.groupby(['year', 'months'], as_index=False, observed=False)['value'].mean()
    plt.figure(figsize=(15, 8))
    sns.barplot(x='year', y='value', hue='months', data=df_grouped)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.show()
draw_bar_plot(df_clean)
print('\n\n\n')
#3. Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data
def draw_box_plot(values):
    values_df = values.copy()
    values_df['year'] = values['date'].dt.year
    values_df['months'] = values['date'].dt.month_name()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    values_df['months'] = pd.Categorical(values_df['months'], categories=month_order, ordered=True)
    
    palette = sns.color_palette("deep", n_colors=4)
    palette_1 = sns.color_palette("deep", n_colors=12)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 9))
    
    # Draw boxplot for years
    sns.boxplot(x='year', y='value', hue='year', data=values_df, palette=palette, fill=True,  linecolor='black', legend=False, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_ylabel('Page Views')
    # Draw boxplot for months
    sns.boxplot(x='months', y='value', hue='months', data=values_df, palette=palette_1, legend=False, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()
    plt.show()
    
draw_box_plot(df_clean)
