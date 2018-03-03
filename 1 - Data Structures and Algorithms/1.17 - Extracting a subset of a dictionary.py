#!environment/bin/python3
"""
You want a subset of another dictionary.
"""
# Dictionary comprehension

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20
}

p1 = {key:value for key, value in prices.items() if value>200}

# or

tech=['AAPL', 'IBM', 'HPQ', 'MSFT']
p2 = {key:value for key,value in prices.items() if key in tech}
