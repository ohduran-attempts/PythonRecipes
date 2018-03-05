#!environment/bin/python3
"""
You want to create a string in which embedded variable names
are substituted with a string representation of a variable's value.
"""

s = '{name} has {n} messages.'

print(s.format(name='Alvaro', n=37)) # Alvaro has 37 messages.

name = 'Alvaro'
n = 37

print(s.format_map(vars())) # Alvaro has 37 messages.

# One feature of vars() is that it also works with classes.

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Alvaro', 37)

print(s.format_map(vars(a))) # Alvaro has 37 messages.

""" These do not work well with missing values. Try 'frame hack' instead."""
