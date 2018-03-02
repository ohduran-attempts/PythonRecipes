#!environment/bin/python3
"""
You want to implement a queue that sorts items
by a given priority and always returns
the item with the highest priority on each pop.
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority,self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


"""And here it's how it is used:"""
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

"""
heapq.heappush and heapq.heappop insert and remove items from a list
in a way such that the first item in the list has the smallest priority,
with O(log N) complexity. In this recipe, the queue consists of tuples
of the form (-priority, index, item), which means priority from mayor to minor,
and index to properly order items with the same priority level, sorting them
according to the order in which they were inserted, and avoid problems with
items that cannot be sorted (as in, they are not numbers).
"""
