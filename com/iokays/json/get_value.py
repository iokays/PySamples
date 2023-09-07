#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json

data = ''

# 将JSON对象转换为Python字典
data_dict = json.loads(data)

# 创建一个空列表来存储CardNo的值
result = []

# 遍历prepaidCards数组中的每个元素
for card in data_dict["prepaidCards"]:
    # 获取cardNo属性的值，并添加到列表中
    result.append(card["cardNo"])

# 打印列表中的所有CardNo的值
print(result)
