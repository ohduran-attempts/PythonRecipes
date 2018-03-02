#!environment/bin/python3
"""
You want to control the order of items
in a dictionary.
"""

from collections import OrderedDict

d = OrderedDict()

d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key,d[key])

"""This can be useful when creating a JSON file"""
import json
print(json.dumps(d))

# An OrderedDict internally maintains a doubley linked list that orders the keys
# according to insertion order.
