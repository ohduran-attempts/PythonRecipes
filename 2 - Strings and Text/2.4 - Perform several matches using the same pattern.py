#!environment/bin/python3
"""
Perform a lot of matches using the same pattern.
"""

# Precompile the reg ex pattern into a pattern object first.
import re
datepat = re.compile(r'\d+/\d+/\d+') # date pattern

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

print(datepat.match(text1))
# <_sre.SRE_Match object; span=(0, 10), match='11/27/2012'>

print(datepat.match(text2))
# None
