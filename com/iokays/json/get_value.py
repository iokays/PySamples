#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
from jsonpath import jsonpath


def get_value(content: str, path: str):
    # 将JSON对象转换为Python字典
    data_dict = json.loads(content)
    return jsonpath(data_dict, path)


print(get_value('{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}', '$.hometown.name'))

#
# $.store.book[*].author	store中的所有的book的作者
# $…author	                所有的作者
# $.store.*	                store下的所有的元素
# $.store…price	            store中的所有的内容的价格
# $…book[2]	                第三本书
# $…book[(@.length-1)]	$…book[-1:]
# $…book[0,1]	$…book[:2]
# $…book[?(@.isbn)]	        获取有isbn的所有数
# $…book[?(@.price<10)]	    获取价格大于10的所有的书
# $…*	                    获取所有的数据

