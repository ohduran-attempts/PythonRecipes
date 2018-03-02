"""You have an N-element tuple or sequence that you would like to unpack into a collection of N variables."""

a, b = (4, 5)
print(a)  # 4
print(b)  # 5

data = ['ACME', 50, 91.1, (2012, 12, 21)]

name, shares, price, (year, mon, day) = data

print(day, mon, year)  # (21,12,2012)

s = 'Hello'
a, b, c, d, e = s

print(a, b, e)  # ('H', 'e', 'o')
