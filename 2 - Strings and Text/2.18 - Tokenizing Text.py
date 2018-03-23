#!environment/bin/python3
"""
You have a string that you want to parse
 left to right into a stream of tokens.
"""
import re
from collections import namedtuple
text = 'foo = 23 + 42 * 10'
# Have some way to identify the kind of pattern as well as match it.

# ?P<TOKENNAME>
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z__0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>\=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# Now, scanner goes one match at a time on the compiler.
# We can build a generator.

# namedtuple is a short class named Token with values type and value
Token = namedtuple('Token', ['type', 'value'])


def generate_tokens(pat, text):
    """Generate a token based on a text under a certain pattern."""
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


for tok in generate_tokens(master_pat, text):
    print(tok)
