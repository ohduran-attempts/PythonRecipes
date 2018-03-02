#!environment/bin/python3
"""
You want to eliminate duplicates in a sequence while preserving order.
"""

#If all you want to do is remove duplicates, use set(a)
a = [7,1,2,4,6,4,5,2,4,3,5,10,6,10]
print(set(a)) # {1, 2, 3, 4, 5, 6, 7,10}
# However, order isn't preserved.


# When values are hashable
def dedupe1(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

# When values are not hashable (like dicts):
def dedupe(items, key=None):
    """ The key argument specifies a function that convert
        sequence items into a hashable type for duplicate detection."""
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

"""This removes duplicated x"""
c = list(dedupe(a,key=lambda d: d['x']))
print(c) # [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

"""This removes duplicated x AND y"""
b = list(dedupe(a, key=lambda d: (d['x'],d['y'])))
print(b) # [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
