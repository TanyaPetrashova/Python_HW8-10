"""Задача 40:
Работать с файлом california_housing_train.csv, который находится в папке sample_data.
Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)."""

import pandas as pd

df = pd.read_csv('sample_data/california_housing_train.csv')

filtered_df = df[(df['population'] >= 0) & (df['population'] <= 500)]

print(filtered_df.head())

mean_house_valie = filtered_df['median_house_value'].mean()

print(mean_house_valie)