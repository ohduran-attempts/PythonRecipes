#!environment/bin/python3
"""
You are trying to match a text pattern using regex,
but it is identifying the longest possible matches of a pattern.
Instead, you would like to change it to find
the shortest possible match.
"""

# Ilustrate:
import re
str_pat = re.compile(r'\"(.*)\"')

text1 = 'Computer says "no."'
print(str_pat.findall(text1)) # ['no.']

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2)) # ['no." Phone says "yes.']

# The problem has to do with the * wildcard in the pattern,
# so matching is based on the longest possible match.

str_pat2 = re.compile(r'\"(.*?)\"')
print(str_pat2.findall(text2)) # ['no.', 'yes.']

""" the ? makes the * limited,
so that it produces the shortest match instead."""
