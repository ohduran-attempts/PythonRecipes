#!environment/bin/python3
"""
You need to unpack N elements from an iterable, but the iterable
may be longer than N elements, causing an error.
"""


def avg(l):
    """Average."""
    return sum(l) / len(l)


def drop_first_last(grades):
    """
    From a list, drop the first and the last elements
    and calculate average.
    """
    first, *middle, last = grades
    return avg(middle)


print(drop_first_last([1,2,3,5]))

def do_one(x,y):
    print(1,2,3)
def do_four(x):
    print(4,5)

records = [(1,2,3),(4,5)]
for tag, *args in records:
    if tag == 1:
        do_one(*args)
    if tag == 4:
        do_four(*args)

items = [7,6,5,4,6,5]
head, *tail = items
print(head) # 7
print(tail) # (6,5,4,6,5)
