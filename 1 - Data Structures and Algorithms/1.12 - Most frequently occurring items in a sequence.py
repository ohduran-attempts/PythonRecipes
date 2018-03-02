#!environment/bin/python3
"""
Determine frequency of items
in a sequence.
"""
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]

"""Counts can be combined"""
c = word_counts + word_counts
print(c.most_common(6))
# [('eyes', 16), ('the', 10), ('look', 8), ('into', 6), ('my', 6), ('around', 4)]
