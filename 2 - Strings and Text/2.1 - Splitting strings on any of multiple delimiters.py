#!environment/bin/python3
"""
You want to split a string into fields, but the delimiters aren't consistent.
"""

line = 'asdf fjdk; afed, fjek,asdf, foo'

from re import split

fields = split(r'[;,\s]\s*', line)
print(fields)
