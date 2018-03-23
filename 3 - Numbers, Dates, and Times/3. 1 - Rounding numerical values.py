#!environment/bin/python3
"""
You want to round a floating point number
to a fixed number of decimal places.
"""
print(round(1.23, 1))  # 1.2

print(round(1.25362, 3))  # 1.254

# The number of digits given can be negative, and it means rounding
# for tens, hundreds, ...

a = 16277
print(round(a, -3))  # 16000
