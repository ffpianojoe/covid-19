# importing necessary modules

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import covid as cv

# reading in .csv file and setting datetime column for easier analysis
df = pd.read_csv('new_data.csv')
df['datetime'] = pd.to_datetime(df['date'])
df = df.set_index('datetime')
df.drop(['date'], axis=1, inplace=True)

# examining the top countries for total cases and total deaths based on EDA findings
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

# 2020 Population numbers retrieved from Our World in Data
us_pop = 331002647
sp_pop = 46754783
it_pop = 60461828
germ_pop = 83783945
china_pop = 1439323774
fran_pop = 65273512
iran_pop = 83992953
uk_pop = 67886004
turk_pop = 84339067
swiss_pop= 8654618
nether_pop = 17134873
belg_pop = 11589616

# Tracking the Case Fatality Rate
world_death = cv.death_over_time(world, 60)
german_death = cv.death_over_time(germany, 60)
us_death = cv.death_over_time(us, 60)
sp_death = cv.death_over_time(spain, 60)
it_death = cv.death_over_time(italy, 60)
print(german_death.tail(10))

# Plotting relative to total population
sns.set()
world_death.plot(linewidth=5)
german_death.plot()
us_death.plot()
sp_death.plot()
it_death.plot()
plt.legend(['Global', 'Germany', 'United States', 'Spain', 'Italy'])
plt.title('Global Case Fatality Rate - COVID-19')
plt.xlabel('Date')
plt.ylabel('Case Fatality Rate')
plt.show()
