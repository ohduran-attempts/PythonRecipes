#!environment/bin/python3
"""
You have a list of dictionaries and you would like
to sort the entries according to
one or more of the dictionary values.
"""

rows = [
{'fname':'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname':'David', 'lname': 'Beazley', 'uid': 1002},
{'fname':'John', 'lname': 'Cleese', 'uid': 1001},
{'fname':'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)
# [{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
# {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
# {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]

rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)
# [{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
# {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
# {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
# {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]

""" itemgetter can accept multiple keys: """
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)
# [{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
# {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
# {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}]

""" it works faster than sorted(rows, key=lambda r:r['fname'])."""
