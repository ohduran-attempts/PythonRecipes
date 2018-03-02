#!environment/bin/python3
"""
You want to sort objects of the same class, but they don't natively
support comparison.
"""

# sorted(rows, key=lambda r: r.attribute)

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]

print(users) # [User(23), User(3), User(99)]
print(sorted(users, key=lambda u:u.user_id))
# [User(3), User(23), User(99)]

""" Analogous to itemgetter, we can use attrgetter
(this is even faster): """
from operator import attrgetter

print(sorted(users, key=attrgetter('user_id')))
# [User(3), User(23), User(99)]
