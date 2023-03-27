"""Задача 40:
Работать с файлом california_housing_train.csv, который находится в папке sample_data.
Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)."""

import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')

filtered_df = df[(df['population'] >= 0) & (df['population'] <= 500)]

print(filtered_df.head(10))

mean_house_valie = filtered_df['median_house_value'].mean()

print('Средняя стоимость дома, где количество людей от 0 до 500 --> ', mean_house_valie)

""" Задача 42:
Узнать какая максимальная households в зоне минимального значения population. """

min_population = df['population'].min()

filtered_df2 = df[df['population'] == min_population]

max_households = filtered_df2['households'].max()

print("Максимальное значение households в зоне с минимальным значением population: ", max_households)