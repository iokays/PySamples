#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pandas as pd

crime = pd.read_csv('./exercise_data/US_Crime_Rates_1960_2014.csv')
print(crime.head())
print(crime.info())

crime.Year = pd.to_datetime(crime.Year, format='%Y')
print(crime.head())

crime = crime.set_index('Year', drop=True)
print(crime.head())

del crime['Total']
print(crime.head())

print('####################')
print(crime.resample('10AS').sum())

# 用resample去得到“Population”列的最大值
print(crime['Population'].resample('10AS').max())

print('####################')
print(crime.idxmax(0))


