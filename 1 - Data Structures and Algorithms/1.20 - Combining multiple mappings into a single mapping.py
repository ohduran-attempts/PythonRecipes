#!environment/bin/python3
"""
you have multiple dictionaries or mappings that you want to logically combine
into a single mapping to perform certain operations,
such as looking up values or checking for existence of keys.
"""

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

# First check a, then b if not found.

from collections import ChainMap
c = ChainMap(a,b)

print(c.keys()) #x,y,z  (duplicates imply that the one in a gets picked.)
