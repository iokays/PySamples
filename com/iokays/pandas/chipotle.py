#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pandas as pd

chipo = pd.read_csv('./exercise_data/chipotle.tsv', sep='\t')
print(chipo.head(10))
print(chipo.shape[0])
print(chipo.shape[1])
print(chipo.columns)
print(chipo.index)

c = chipo[['item_name', 'quantity']].groupby(['item_name'], as_index=False).agg({'quantity': 'sum'})
c.sort_values(['quantity'], ascending=False, inplace=True)

print(c.head(10))

print(chipo['item_name'].nunique())

print(chipo['choice_description'].value_counts().head())

print(chipo['quantity'].sum())

# 步骤13 将item_price转换为浮点数
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:-1]))
print(chipo.head())


# 步骤14 在该数据集对应的时期内，收入(revenue)是多少
chipo['sub_total'] = round(chipo['quantity'] * chipo['item_price'], 2)
print(chipo.head())

# 步骤15 在该数据集对应的时期内，一共有多少订单？
print(chipo['order_id'].nunique())

# 每一单(order)对应的平均总价是多少？
print(chipo[['order_id', 'sub_total']].groupby(['order_id'], as_index=False).agg({'sub_total': 'sum'})['sub_total'].mean())

# 一共有多少种不同的商品被售出？
print(chipo['item_name'].nunique())



