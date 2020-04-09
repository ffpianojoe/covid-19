# importing necessary modules

import pandas as pd
import covid as cv

# reading in .csv file and setting datetime column for easier analysis
pd.set_option('display.max_columns', 10)
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
swiss_pop = 8654618
nether_pop = 17134873
belg_pop = 11589616

world_dot = cv.death_over_time(world, 30)
print(world_dot.tail())

# Taking a closer look at hardest-hit areas and comparing with Germany, which has an unusually low CFR
print(world.tail())
print(us.tail())
print(spain.tail())
print(italy.tail())
print(germany.tail())
print(china.tail())

# Printing details of the countries most impacted as found in our EDA
cv.print_data(world)
cv.print_data(us)
cv.print_data(spain)
cv.print_data(italy)
cv.print_data(germany)
cv.print_data(china)
cv.print_data(france)
cv.print_data(iran)
cv.print_data(uk)
cv.print_data(turk)
cv.print_data(swiss)
cv.print_data(nether)
cv.print_data(belg)

us2 = cv.add_data(us, us_pop)
spain2 = cv.add_data(spain, sp_pop)
italy2 = cv.add_data(italy, it_pop)
germany2 = cv.add_data(germany, germ_pop)
turk2 = cv.add_data(turk, turk_pop)
swiss2 = cv.add_data(swiss, swiss_pop)
print(us2.tail())
print(spain2.tail())
print(italy2.tail())
print(germany2.tail())
print(turk2.tail())
print(swiss2.tail())

german_death = cv.death_over_time(germany, 60)
print(german_death.tail(10))
