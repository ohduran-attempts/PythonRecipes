#!environment/bin/python3
"""
You want to make a dictionary that maps keys to more than one
value (so-called 'multidict').
"""

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(4)

# Two ways of doing the same thing:

d = {}
pairs = [(1,2),(3,4)]
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

e = defaultdict(list)
for key,value in pairs:
    e[key].append(value)
