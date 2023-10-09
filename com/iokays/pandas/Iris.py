#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pandas as pd

iris = pd.read_csv('./exercise_data/iris.csv', names = ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'class'])
print(iris.head(10))

print(pd.isnull(iris).sum())

iris.petal_length.fillna(1, inplace = True)

print(iris.head(10))

del iris['class']
print(iris.head(10))

iris = iris.dropna(how='any')
print(iris.head(10))

iris = iris.reset_index(drop=True)
print(iris.head(10))



