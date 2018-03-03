#!environment/bin/python3
"""
You need to search for an possibly replace text in case-insensitive manner.
"""
text = 'UPPER PYTHON, lower python, Mixed Python.'

import re
x = re.findall('python', text, flags=re.IGNORECASE)
print(x) # ['PYTHON', 'python', 'Python']

y = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(y) # UPPER snake, lower snake, Mixed snake.

# It's limited, but you might want to try this:
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
