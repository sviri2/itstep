# def gamravleba(a, b):
#     print(a*b)
    
# gamravleba(5, 10)


# def my_func(x):
#     print(x*x - 5*x)
    
# my_func(5)  
# my_func(10)
# my_func(-4)

# def multyplay(a, b):
#     return a * b

# def ekranze_gamotana():
#  print(multyplay(10, 20))

# ekranze_gamotana()

# def multiply(a, b):
#  return a * b
# print(multiply(10, 5))

# def greetings(name, surname):
#     print("welcome", name, "your surname is", surname)
    
from re import X


def my_func(arr):
    for i in range(len(arr)):
     arr[i] = arr[i] ** 2
     
    return arr
print(my_func([3, 5, 6, 34]))
    