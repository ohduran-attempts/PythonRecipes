#!environment/bin/python3
"""
You have code that accesses list or tuple elements by position,
but this makes the code difficult to read.

You want to access the elements by name.
"""

from collections import namedtuple

Subscriber = namedtuple('Subscriber',['addr', 'joined'])
sub = Subscriber('jones@example.com', '2012-10-19')

print(sub.addr) # jones@example.com
print(sub.joined) # 2012-10-19
len(sub) # 2
addr,joined = sub
print(addr)  # jones@example.com

"""A major use case for this is decoupling your code
from the position of the elements it manipulates.
"""

Stock = namedtuple('Stock',['name','shares','price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec) # out of the dictionary of records, take each one
        total += s.shares * s.price
    return total

"""namedtuple can be a replacement for a dictionary,
but be aware that it will be immutable."""
