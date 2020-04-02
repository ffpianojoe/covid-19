import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def calc_data(country):
    cases = country['total_cases'][-1]
    deaths = country['total_deaths'][-1]
    rate = country['total_deaths'][-1] / country['total_cases'][-1]
    location = country['location'][0]
    return cases, deaths, rate, location


def print_data(data):
    output = calc_data(data)
    print(output[3])
    print('Total Cases: ', output[0])
    print('Total Deaths: ', output[1])
    print('Case Fatality Rate: {:.2%}'.format(output[2]))


def death_over_time(data, start=0):
    rate = data['total_deaths'] / data['total_cases']
    return rate.iloc[start:]


df = pd.read_csv('new_data.csv')

df['datetime'] = pd.to_datetime(df['date'])
df = df.set_index('datetime')
df.drop(['date'], axis=1, inplace=True)

# print(df.head())
# print(df.info())

us = df[df['location'] == 'United States']
italy = df[df['location'] == 'Italy']
china = df[df['location'] == 'China']
spain = df[df['location'] == 'Spain']
germany = df[df['location'] == 'Germany']
france = df[df['location'] == 'France']
uk = df[df['location'] == 'United Kingdom']
iran = df[df['location'] == 'Iran']
world = df[df['location'] == 'World']
swiss = df[df['location'] == 'Switzerland']
canada = df[df['location'] == 'Canada']

world_dot = death_over_time(world, 30)
print(world_dot.head(10))
print(world_dot.tail(10))

print(world.pivot_table(index=world.index, values='total_cases').tail())

print_data(world)
print_data(us)
print_data(italy)
print_data(china)
print_data(spain)
print_data(germany)
print_data(france)
print_data(uk)
print_data(iran)
print_data(swiss)
print_data(canada)

print(china.tail())
print(us.tail())
print(italy.tail())
print(spain.tail())

sns.set()
world_dot.plot()
x = us['2020-03-01':].index
y = us['2020-03-01':].total_cases
x2 = italy['2020-03-01':].index
y2 = italy['2020-03-01':].total_cases
x3 = spain['2020-03-01':].index
y3 = spain['2020-03-01':].total_cases
# plt.plot(x, y, marker='.', linestyle='-')
# plt.plot(x2, y2, marker='.', linestyle='-')
# plt.plot(x3, y3, marker='.', linestyle='-', color='red')
# plt.legend(['US', 'Italy', 'Spain'])
# plt.title('COVID-19 Total Cases - US/Italy/Spain')
plt.title('Case Fatality Rate Over Time - Global')
plt.xlabel('Date')
plt.ylabel('Case Fatality Rate')
# plt.show()