# importing necessary modules

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# reading in .csv file and setting datetime column for easier analysis
df = pd.read_csv('new_data.csv')
df['datetime'] = pd.to_datetime(df['date'])
df = df.set_index('datetime')
df.drop(['date'], axis=1, inplace=True)

# Taking an initial look at the data
print(df.head())
print(df.info())
print(df.describe())

# Finding the top 10 countries for total cases and total deaths
cases = df.pivot_table(index='location', values='new_cases', aggfunc=sum)
print(cases.sort_values('new_cases', ascending=False).head(11))
deaths = df.pivot_table(index='location', values='new_deaths', aggfunc=sum)
print(deaths.sort_values('new_deaths', ascending=False).head(11))

# Specifying the top countries as found in the exploration above
world = df[df['location'] == 'World']
us = df[df['location'] == 'United States']
spain = df[df['location'] == 'Spain']
italy = df[df['location'] == 'Italy']
germany = df[df['location'] == 'Germany']
china = df[df['location'] == 'China']
france = df[df['location'] == 'France']
iran = df[df['location'] == 'Iran']
uk = df[df['location'] == 'United Kingdom']
turk = df[df['location'] == 'Turkey']
swiss = df[df['location'] == 'Switzerland']
nether = df[df['location'] == 'Netherlands']
belg = df[df['location'] == 'Belgium']

# Plotting points of interest
sns.set()
x, y = us['2020-03-01':].index, us['2020-03-01':].total_cases
x2, y2 = spain['2020-03-01':].index, spain['2020-03-01':].total_cases
x3, y3 = italy['2020-03-01':].index, italy['2020-03-01':].total_cases
x4, y4 = germany['2020-03-01':].index, germany['2020-03-01':].total_cases
plt.plot(x, y, marker='.', linestyle='-')
plt.plot(x2, y2, marker='.', linestyle='-')
plt.plot(x3, y3, marker='.', linestyle='-')
plt.plot(x4, y4, marker='.', linestyle='-')
plt.legend(['US', 'Spain', 'Italy', 'Germany'])
plt.title('Comparing COVID-19 Among Countries with Highest Outbreaks')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.show()
