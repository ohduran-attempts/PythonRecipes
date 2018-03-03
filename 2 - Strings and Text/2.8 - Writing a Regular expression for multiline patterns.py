#!environment/bin/python3
"""
Match a block of text using a regex,
but you need the match to span multiple lines.
"""

# Typically arises in patterns that use the dot to match
# any character but forget to account for the fact
# that it doesn't match newlines.
import re
comment = re.compile(r'/\*(.*?)\*/')

text = ''' /* This is a
multiline comment */
'''
print(comment.findall(text)) # []

# Expand the meaning of the dot wildcard with \n
comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')

print(comment2.findall(text))
# [' This is a\nmultiline comment ']
