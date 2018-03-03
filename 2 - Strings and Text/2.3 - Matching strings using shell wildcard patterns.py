#!environment/bin/python3
"""
You want to match text using Unix shell wildcards.
"""

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt','*.txt'))   # True
print(fnmatch('foo.txt','?oo.txt')) # True

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

print([name for name in names if fnmatch(name, 'Dat*.csv')])
# ['Dat1.csv', 'Dat2.csv']

"""Unix is case sensitive."""
print(fnmatch('foo.txt','*.TXT')) # False

# Use fnmatchcase when you want to make sure it's case sensitive
print(fnmatchcase('foo.txt', '*.TXT')) # False

""" Check 2.6 for case insensitive."""
addresses = [
'5412 CLARK ST',
'1060 ADDISON ST',
'1039 GRANVILLE AVE',
'2122 CLARK ST',
'4802 BROADWAY'
]

st = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(st) # ['5412 CLARK ST', '1060 ADDISON ST', '2122 CLARK ST']

q = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(q) # ['5412 CLARK ST']
