#!environment/bin/python3
"""
You want to make a list of the largest or smallest N items in a collection.
"""

import heapq
"""
The heapq module has two functions:
nlargest and nsmallest
that do exactly what you want.
"""

nums = [154664,34,754356,234523,484678467,324524,67896789,436524562345]

print(heapq.nlargest(3,nums)) # [436524562345, 484678467, 67896789]
print(heapq.nsmallest(3,nums)) # [34, 154664, 234523]

portfolio =[
{'name':'IBM', 'shares': 100, 'price': 91.1},
{'name':'AAPL', 'shares': 50, 'price': 543.22},
{'name':'FB', 'shares': 200, 'price': 21.09},
{'name':'HPQ', 'shares': 35, 'price': 31.75},
{'name':'YHOO', 'shares': 45, 'price': 16.35},
{'name':'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap,expensive)

"""
Underneath the covers, they work by first converting the data
into a list where items are ordered as a heap.
If you are looking for the single smallest/largest, then min() or max()
are faster. And if N is near the length of the list, it's faster
to do sorted(items[:N]) or sorted(items[-N:]).
"""
