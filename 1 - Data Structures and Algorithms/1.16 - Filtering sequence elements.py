#!environment/bin/python3
"""
You have data inside of a sequence, and need to extract values or reduce
the sequence using some criteria.
"""
# Assuming something more complex than just using list comprehension:

def is_int(val):
    """True only if val is integer."""
    try:
        x = int(val)
        return True
    except ValueError:
        return False

values = ['1', '2', '-3', '-', '4', 'N/A', '5']
ivals = list(filter(is_int, values))
print(ivals) # ['1', '2', '-3', '4', '5']

""" filter() creates an iterator, os if you want to create a list
of resutls, make sure you also use list() as shown."""
