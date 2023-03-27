"""
Задача 44:
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies? 

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head() 
"""

import pandas as pd
import random

# Создание исходной DataFrame:
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data.head())

# Создание словаря для one hot представления:
oneHot_dictionary = {valie: i for i, valie in enumerate(data['whoAmI'].unique())}
print(oneHot_dictionary)

# Создание DataFrame для one hot представления:
oneHot_data = pd.DataFrame()
for k, value in oneHot_dictionary.items():
    oneHot_data[k] = (data['whoAmI'] == k).astype(int)
print(oneHot_data)

# Объединение исходной DataFrame и DataFrame в one hot представлении:
data = pd.concat([data, oneHot_data], axis=1)   # axis=1 - объединение должно выполняться по столбцам
print(data)                                     # axis=0 - объединение по строкам

# Удаление столбца 'whoAmI':
data.drop('whoAmI', axis=1, inplace=True)
print(data.head())

# Каждый пункт выводила в печать на экран для себя - для более простого понимания.
# Можно было распечатать только результат.