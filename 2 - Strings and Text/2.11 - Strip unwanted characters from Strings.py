#!environment/bin/python3
"""
You want to strip unwanted characters, such as whitespaces.
"""

# strip() method can be used, along with lstrip() and rstrp()
# to strip from the left or right side, respectively.

s = '   hello world \n'

print(s.strip()) # 'hello world'

"""Stripping does not apply to any text in the middle!"""

s = '   hello            world \n'

print(s.strip()) # 'hello            world'

# You can use replace() instead.

print(s.replace(' ','')) # 'helloworld'
