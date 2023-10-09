#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests


content = requests.get("http://www.baidu.com")
print(content.content.decode("utf-8"))

