#!environment/bin/python3
"""
Check the start or end of a string for specific patterns.
filename extensions, URL schemes, ...
"""

filename = 'spam.txt'

print(filename.endswith('.txt')) # True

url = 'http://www.python.org'
print(url.startswith('http:')) # True

# Check against multiple choices by providing a tuple:

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:','https:','ftp:')):  #url
        return urlopen(name).read()
    else:
        with open(name) as f:                       #file
            return f.read()

# It HAS TO BE a tuple. Make sure you convert with tuple first.

choices = ['http','ftp']
url = 'http://www.python.org'
# url.startswith(choice) won't work

url.startswith(tuple(choices)) # True
