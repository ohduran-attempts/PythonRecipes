#!environment/bin/python3
"""
Clean up an unreadable mess.
"""
record = '....................100.......513.25..........'

# Instead of using record[20:32] and record[40:48], use:
SHARES = slice(20,32)
PRICE = slice(40,48)

cost = int(record[SHARES]) * float(record[PRICE]) # much clearer

"""
slice(a,b) acts as a substitute for a:b when slicing a list.
In fact, slice(start,stop,step) works EXACTLY like using [start:stop:step]
"""
