import pandas as pd


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


def add_data(data, population):
    data['total_ratio'] = data['total_cases'] / population
    data['per_mil'] = data['total_cases'] / (population / 1000000)
    data['deaths_per'] = data['total_deaths'] / (population / 1000000)
    return data
