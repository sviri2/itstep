# def name():
#     return "it step"
# nm = name()
# print(nm)
   
# def double(n):
#     return n*2
# a = double(400)
# print(a)

# def sum(a, b):
#     return max(a,b)
# def list(lst):
#     for i in lst:
#         if i %2 == 1:
#             lst.remove(i)
#     return lst       


# # def list(lst)
# def square(list):

    
#     n_list = []
    
#     for i in list:
        
#         n = i ** 2
        
#         n_list.append(n)
        
    
    
#     return n_list   

# def square(*args):
    
#     n_arg = []
    
#     for i in args:
#         n = int(i)**2
#         n_arg.append(n)
#     return n_arg

# print(square("123"))
# import random
# def saxelis_generatori(lst):
#     y = random.choice(lst)
#     return f"გამარჯობა , {y}"
# saxelebi = ["levaniko", "beso", "ika", "nono"]
# print(saxelis_generatori(saxelebi))

# def sigrze(str):
#     trak = 0
#     for i in str:
#         trak += 1
#     return trak
# rao = ("levaniko")
# print(sigrze(rao))

# def square(lst):
#     lst1 = []
#     for i in lst:
#         y = i ** 2
#         lst1.append(y)   
#     return lst1
# cifrebi = [1, 2, 5]
# print(square(cifrebi))   

# def square(numbers):
#     str1 = ""
#     for i in numbers:
#         str1 += str(int(i) ** 2)
#     return str1
# cifrebi = "1243"
# print(square(cifrebi))



import random

def randompasswordgen():
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digit = "1234567890"
    lower_l = "abcdefghijklmnopqrstuvwxyz"
    special = "?&*%$"
    ALL = upper + digit + lower_l + special
    password = ""
    upper1 = random.choice(upper)
    upper2 = random.choice(upper)
    random_digit = random.choice(digit)
    random_special = random.choice(special)
    
    password = upper1 + upper2 + random_digit +random_special
    for i in range(6):
        password += random.choice(ALL)
    return password
        
print(randompasswordgen())
    
    
    
