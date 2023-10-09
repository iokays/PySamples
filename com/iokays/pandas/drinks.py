#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pandas as pd

drinks = pd.read_csv('./exercise_data/drinks.csv')
print(drinks.head())

# 哪个大陆(continent)平均消耗的啤酒(beer)更多？
print(drinks.groupby(['continent']).beer_servings.mean())

# 打印出每个大陆(continent)的红酒消耗(wine_servings)的描述性统计值
print(drinks.groupby(['continent']).wine_servings.describe())

# 打印出每个大陆每种酒类别的消耗平均值
print(drinks.groupby(['continent']).wine_servings.mean())

# 打印出每个大陆每种酒类别的消耗中位数
print(drinks.groupby(['continent']).wine_servings.median())

