#!environment/bin/python3
"""
You want to find out what two dictionaries have in common
(keys and/or values).
"""

a = {
'x' : 1,
'y' : 2,
'z' : 3
}

b = {
'w' : 10,
'x' : 11,
'y' : 2
}

print(a.keys() & b.keys()) # {'y', 'x'} both a and b
print(a.keys() - b.keys()) # {'z'} --> a but not in b
print(a.items() & b.items()) # {('y', 2)}

# Make a new dictionary with certain keys removed:
c = {key:a[key] for key in a.keys() - {'z','w'}}

print(c) # {'x': 1, 'y': 2}
