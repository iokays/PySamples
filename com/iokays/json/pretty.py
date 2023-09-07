#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pretty_json
import json

content = '''

{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}

'''

result = pretty_json.pretty_print(json.loads(content), sort_keys=False, indent=4, separators=(',', ': '))

print(result)
