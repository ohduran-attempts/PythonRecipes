#!environment/bin/python3
"""
Working with Unicode strings, but need to make sure
that all of the strings have the same underlying
representation.
"""

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1,s2) # Spicy Jalapeño Spicy Jalapeño

print(s1==s2) # False

""" Having multiple representations is a problem when matching."""

# Normalise text
import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
# NFC means fully composed - single code point
# Python also supports NFKC and NFKD,
# check http://www.unicode.org/faq/normalization.html

print(t1,t2) # Spicy Jalapeño Spicy Jalapeño
print(t1==t2)# True
