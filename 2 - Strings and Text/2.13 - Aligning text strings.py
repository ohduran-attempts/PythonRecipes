#!environment/bin/python3
"""
Format text with some sort of alignment applied.
"""

# ljust(), rjust() and center() methods.

text = 'Hello world'
print(text.ljust(20)) #'Hello world         '

print(text.rjust(20)) # '         Hello world'

print(text.center(20)) # '    Hello world     '


# Format can also be used.

x = '{:>10s} {:>10s}'.format('Hello', 'World')
print(x) # '     Hello      World'

# It can also be used in numbers:
y = 1.2345

print(format(y, '>10')) # '    1.2345'
