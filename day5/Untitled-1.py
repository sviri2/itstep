from xmlrpc.client import Boolean


def positive_sum(arr):
    my_sum = 0
    for i in arr: 
     if i > 0:
        my_sum += i
        
    return my_sum
