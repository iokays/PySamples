#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pandas as pd

euro12 = pd.read_csv('./exercise_data/Euro2012_stats.csv')

print(euro12.head(10))
print(euro12.Goals)
print(euro12.shape[0])
print(euro12.info)

discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline)

discipline = discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)
print('#############################################')
print(discipline)

print(discipline['Yellow Cards'].mean())

# 找到进球数Goals超过6的球队数据
print(euro12[euro12.Goals > 6])

# 选取以字母G开头的球队数据
print(euro12[euro12.Team.str.startswith('G')])

# 选取前7列
print(euro12.iloc[:, 0:7])

# 选取除了最后3列之外的全部列
print(euro12.iloc[:, :-3])

# 找到英格兰、意大利、俄罗斯的射正率
print(euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team', 'Shooting Accuracy']])
