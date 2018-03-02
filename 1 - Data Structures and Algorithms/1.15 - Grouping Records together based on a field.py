#!environment/bin/python3
"""
You have a sequence of dictionaries or instances and you want
to iterate over the data in groups based on the value of a
field, such as date.
"""

rows = [
{'address': '5412 CLARK', 'date': '07/01/2012'},
{'address': '5148 CLARK', 'date': '07/04/2012'},
{'address': '5800 58TH', 'date': '07/02/2012'},
{'address': '2122 CLARK', 'date': '07/03/2012'},
{'address': '5645 RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 ADDISON', 'date': '07/02/2012'},
{'address': '4801 BROADWAY', 'date': '07/01/2012'},
{'address': '1039 GRANVILLE', 'date': '07/04/2012'}
]

# Iterate over the data in chunks grouped by date by

# 1. sort by the desired field
from operator import itemgetter
rows.sort(key=itemgetter('date'))

# 2. Iterate in groups
from itertools import groupby

for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ',i)
"""
07/01/2012
  {'address': '5412 CLARK', 'date': '07/01/2012'}
  {'address': '4801 BROADWAY', 'date': '07/01/2012'}
07/02/2012
  {'address': '5800 58TH', 'date': '07/02/2012'}
  {'address': '5645 RAVENSWOOD', 'date': '07/02/2012'}
  {'address': '1060 ADDISON', 'date': '07/02/2012'}
07/03/2012
  {'address': '2122 CLARK', 'date': '07/03/2012'}
07/04/2012
  {'address': '5148 CLARK', 'date': '07/04/2012'}
  {'address': '1039 GRANVILLE', 'date': '07/04/2012'}
"""
