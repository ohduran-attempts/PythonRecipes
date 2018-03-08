#!environment/bin/python3
"""
Replace HTML or XML entities such as &entity, or &#code; with their corresponding
text.
"""

s = "Elements are written as <tag>text>/tag>"
import html
print(s)
print(html.escape(s))

from html.parser import HTMLParser
p = HTMLParser()

s = 'Spicy &quot;Jalape&#241;o&quot.'

print(p.unescape(s))
