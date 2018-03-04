#!environment/bin/python3
"""
Handling Unicode characters properly.
"""

# \d already matches any unicode character.

import re
num = re.compile(r'\d+')

print(num.match('123'))
print(num.match('\u0661\u0662\u0663')) #match Arabic digits

"""If you need to include specific Unicode characters,
you can use the usual escape sequence."""

arabic = re.compile(r'[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

# See how to normalise and sanitise all text to a standard form in 2.9.
