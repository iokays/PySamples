#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pandas as pd

apple = pd.read_csv('./exercise_data/Apple_stock.csv')
print(apple.head(10))

print(apple.dtypes)

apple.Date = pd.to_datetime(apple.Date)
print(apple.head())

apple = apple.set_index('Date')
print(apple.head())

print(apple.index.is_unique)

apple = apple.sort_index(ascending=True)
print(apple.head())

print(apple.index.max() - apple.index.min())

appl_open = apple['Adj Close'].plot(title = "Apple Stock")

# changes the size of the graph
fig = appl_open.get_figure()
fig.set_size_inches(13.5, 9)

apple_month = apple.resample("BM")
print(apple_month.head())





