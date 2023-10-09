#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pandas as pd
import datetime

data = pd.read_table('./exercise_data/wind.data', sep='\s+', parse_dates=[[0, 1, 2]])
data.head(10)


