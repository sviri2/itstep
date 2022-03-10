# # dictionary არის სია რომელშიც არის წყვილები წაროდგენილი შემდეგი სახით
# # იწერება {}
# # key:value
# # ეს სია არის changeable ordered noduplicates

# # my_dict = {
# #            "name": "beso",
# #            "surname": "tsakadze",
# #            "age": 45,
# #            "location": "sviri",
        
# #            }
# # print(my_dict)
# # my_dict(age)
# from unicodedata import name


my_dict = {
    "name": "beso",               #string
    "surname": "tsakadze",        #string
    "age": 45 ,                   #int
    "location": "sviri" ,         #string
    "children": ["ika","levani", "ezekia"]   #list
}

print(my_dict["location"])
print(my_dict["surname"])
print(my_dict["children"][:2])
my_dict["age"] = 46                  #ახალი მნიშვნელობის მინიჭება არსებულ სიას
print(my_dict)


# couple_dict = {
#     "beso" : {
#         "name": "beso",
#         "age": 45,
#         "surname": "tsakadze"},
#     "nino" : {
#        "name": "nino",
#        "age": 39,
#        "surname": "bliadze"
#     }
# }
# print(len(couple_dict))

# my_dict = {
#      "name": "beso",               
#      "surname": "tsakadze",        
#      "age": 45 ,                   
#      "location": "sviri" ,         
#      "children": ["ika","levani", "ezekia"]  
#  }

#  my_dict["age"] = 55
#  print(my_dict)

# ვერ გავაკეთე