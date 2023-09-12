#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pretty_json
import json


def pretty(content: str):
    print(json.loads(content))
    result = pretty_json.pretty_print(json.loads(content), sort_keys=False, indent=4, separators=(',', ': '))
    print(result)
    return result


pretty('''
{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}
''')


