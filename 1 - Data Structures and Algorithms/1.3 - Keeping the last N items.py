#!environment/bin/python3
"""
You want to keep a limited history of the last few items seen
during iteration or else.
"""

"""
Using deque creates a fixed-size queue. When new items are added
and the queue is full, the oldest is automatically removed.
You could manually perform such operation, but the queue solution
is more elegant and faster.
"""

from collections import deque

def search(lines, patter, N=5):
    """Simple text match on a sequence of lines,
        yields the matching line along with the previous N lines.
    """
    previous_lines = deque(maxlen=N)
    for line in lines:
        if pattern in line:
            yield line, previous_lines # see 4.3
        previous_lines.append(line)

"""deque can be used whenever you need a simple qeue structure,
    by not stating a maxlen."""
    
