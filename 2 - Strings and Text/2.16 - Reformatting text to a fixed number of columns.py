#!environment/bin/python3
"""
You have a long string that you want to reformat
so that they fill a user-specified number of columns.
"""
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
print(textwrap.fill(s,70)) # 70 char length

print(textwrap.fill(s,40, initial_indent='  ')) #indent
print(textwrap.fill(s,40, subsequent_indent='  ')) # consistent indent across all lines.

""" Check terminal size by using:"""

import os
os.get_terminal_size().columns
