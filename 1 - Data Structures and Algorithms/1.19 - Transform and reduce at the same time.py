#!environment/bin/python3
"""
You want to reduce and filter at the same time.
"""

# Generator-expression argument

# sum of squares
nums = [1,2,3,4,5]
sum(x * x for x in nums)
# LOOK, no need for extra brackets
# that creates an unnecessary temporary list

# if any .py files exist in a directory
import os
files = os.listdir('/')
if any(name.endswith('.py') for name in files): # LOOK
    print(True)
else:
    print(False)

# Output a tuple as a CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))
