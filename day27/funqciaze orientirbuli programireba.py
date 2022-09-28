from itertools import *
from functools import *

def double(x):
    return x*2

def two_sum(x, y):
    return(x+y)


def less_then_five(x):
    return x < 5

def isodd(x):
    return x % 2 == 1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [3, 7, 6, 8, 10, 9, 12, 14]
list3 = [24, 15, 11, 190, -23, 12]
list4 =[1,2,3,4]

#takewhile

# print(list(takewhile(less_then_five, list1)))
# print(list(takewhile(isodd, list2)))

#dropwhile

# print(list(dropwhile(less_then_five, list3)))

#zip
# print(list(zip(list2, list1, list3)))
#filter

# print(list(filter(less_then_five, list3,)))
#map

# print(list(map(double, list1)))

# def func(x):
#     return x*2


# func =lambda x:x**2

# def divfilter(lst, k):
#     return list(filter(lambda x:x % k ==0, list1))

# print (divfilter(list1, 2))
# def oddsum(lst):
#     return sum(list(filter(lambda x:x % 2 == 1, lst)))

# print (oddsum(list1))
#enumerate
# print(list(enumerate(list2)))
# print(sorted(list3))
# print(sorted(list3, reverse = True))

list5 = ["beso", "dato", "levani", "ika"]

# print(sorted(list5, key = lambda x:len(x)))
# print(sorted(list5, reverse = True,  key = lambda x:len(x)))








