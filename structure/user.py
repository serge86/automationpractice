# import random
#
# from structure.pages.home_page import User
#
# # user = User("Ivan", "Popov", "154@gmail.com", "12345", "8",
# #                "12", "1905", "AAAA", "Lviv", "6", "56789", "United States", "123456789", "444@gmail.com")
#
# user = User("Ivan", "Popov", "154@gmail.com", "12345", "8",
#                "12", "1905", "AAAA", "Lviv", "6", "56789", "United States", "123456789", "444@gmail.com")
# # print('\n'.join(repr(u) for u in globals() if not u.startswith('__'))
#
# for i in range(1):
#     globals()[''.join(random.sample(user,random.randint(3,26)))] = random.choice(user)
#
# print
#
# print ('\n'.join(repr((u,globals()[u])) for u in globals() if not u.startswith('__')))

# def random_user()


#
# class AutoAttr(object):
#     def __init__(self, first_name, last_name, email, password, day, month, year, address, city, state, post_code, country, mobile_phone, alias, *args, **kwds):
#         self.data = first_name, last_name, email, password, day, month, year, address, city, state, post_code, country, mobile_phone, alias, *args, **kwds
#     def __get__(self, obj, cls=None):
#         first_name, last_name, email, password, day, month, year, address, city, state, post_code, country, mobile_phone, alias, args, kwds = self.data
#         setattr(obj, first_name, last_name, email, password, day, month, year, address, city, state, post_code, country, mobile_phone, alias (*args, **kwds))
#         print(first_name)
#         return getattr(obj, first_name)
#
#
# import math
# import random
#
# class Test(object):
#     r = AutoAttr('r', random.randrange, 0, math.pow(2,128)-1)  # default value
#     def __init__(self, r=None):
#         if r is not None:  # argument value supplied to override default?
#             self.r = r
#         print format(self.r, ',d')
#
# for i in xrange(5):
#     Test()
# Test(42)  # override default random initial value
#
# import random
#
#     def random.choice([user_1, user_2, user_3])

from operator import itemgetter

# we can store test data in this module like users


# from structure.pages.home_page import User
#
# user = User("Ivan", "Popov", "154@gmail.com", "12345", "8", "12", "1905", "AAAA", "Lviv",
#             "6", "56789", "United States", "123456789", "444@gmail.com")
#
# user_1 = User("Dodo", "Dodov", "487@gmail.com", "85741", "9", "10", "1975", "CDDS",
#               "London", "7", "56789", "United States", "123456789", "487@gmail.com")
#
# user_2 = User("Manu", "Manuv", "587@gmail.com", "85741", "25", "4", "1992", "KUTB",
#               "Riga", "43", "56789", "United States", "123456789", "587@gmail.com")
#
# user_3 = User("Nicola", "Nicolenko", "187@gmail.com", "12741", "15", "6", "1992", "KUTB",
#               "Oslo", "13", "56789", "United States", "123456789", "187@gmail.com")

users = [
    {"first_name": "Ivan", "last_name": "Popov", "email": "227@gmail.com", "password": "12345", "day": "8",
     "month": "12", "year": "1905", "address": "AAAA", "city": "Lviv", "state": "6", "post_code": "56789",
     "country": "United States", "mobile_phone": "123456789", "alias": "227@gmail.com"},
    {"first_name": "Dodo", "last_name": "Dodov", "email": "487@gmail.com", "password": "85741", "day": "9",
     "month": "10", "year": "1975", "address": "CDDS", "city": "London", "state": "7", "post_code": "56789",
     "country": "United States", "mobile_phone": "123456789", "alias": "487@gmail.com"},
    {"first_name": "Manu", "last_name": "Manuv", "email": "587@gmail.com", "password": "85741", "day": "25",
     "month": "4", "year": "1992", "address": "KUTB", "city": "Riga", "state": "43", "post_code": "56789",
     "country": "United States", "mobile_phone": "123456789", "alias": "587@gmail.com"},
    {"first_name": "Nicola", "last_name": "Nikolenko", "email": "187@gmail.com", "password": "12741", "day": "15",
     "month": "6", "year": "1992", "address": "KUTB", "city": "Oslo", "state": "13", "post_code": "56789",
     "country": "United States", "mobile_phone": "123456789", "alias": "187@gmail.com"},
]


def get_user(first_name):
    try:
        return (user for user in users if user["first_name"] == first_name).next()
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % first_name)
