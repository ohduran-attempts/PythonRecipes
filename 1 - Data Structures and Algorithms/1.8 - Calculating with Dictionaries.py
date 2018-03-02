#!environment/bin/python3
"""
You want to perform various calculations (min, max, sort)
on a dictionary of data.
"""

prices = {

'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

# Using zip:
min_price = min(zip(prices.values(),prices.keys()))
print(min_price) # (10.75, 'FB')

max_price = max(zip(prices.values(),prices.keys()))
print(max_price) # (612.78, 'AAPL')

prices_sorted = sorted(zip(prices.values(),prices.keys()))
print(prices_sorted)
# [(10.75, 'FB'),
# (37.2, 'HPQ'),
#(45.23, 'ACME'),
# (205.55, 'IBM'),
# (612.78, 'AAPL')]

"""
When performing common data reductions on a dictionary,
you'll find that they only process keys, not values.
Maybe trying max(prices.values()) will do in some cases,
but not always.

You may want to know information about the corresponding key!
Thus, you can get the key corresponding to the min/max value
if you supply a key.
"""
x = min(prices, key=lambda k: prices[k])
print(x) # FB --> Just the key

xy = prices[x]
print(xy) # 10.75 --> Just the value

"""
zip() solves the problem by inverting the dictionary
into a sequence of (value, key) pairs. When comparing,
the value element is compared first, followed by the key.
"""
