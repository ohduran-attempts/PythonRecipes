#!environment/bin/python3
"""
You want to search and replace a text pattern in a string.
"""

text = 'yeah, but no, but yeah, but no, but yeah'

t = text.replace('yeah', 'yes')

print(t)
# yes, but no, but yes, but no, but yes

""" For more complex patterns, use sub() in re module."""
import re
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

x = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
# Backslashed digits such as \3 refer to capture group number 3 in first pattern.
print(x) # Today is 2012-11-27. PyCon starts 2013-3-13.
