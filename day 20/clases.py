#OOP object orientinted programming
#სადავ ვქმნიტ ობიექტებს ,მაგრამ ამისტვის ვიყენებთ  class  ებს template ად შაბლონებად
#მეთოდი არის class ის შიგნით არსებული ფუნქცია,რომელიც ეკუტვნის მის ყველა პოტენციურ ობიექტს


# class Student:
#     #iq = 120  #atribute
#     def __init__(self, iq, name, surname, grade):  #constractor function
#         self.iq = iq
#         self.name = name
#         self.surname = surname
#         self.grade = grade
        
#     def say_hello(self):
#         return "მე მქვია" + self.name
    
#     #creating instance for the class
    
# beso = Student(120, "ბესო", "წაქაძე", "5")
# jumber = Student(110, "ჯუმბერი", "ტყაბლაძე", 3)
# print (beso.iq)
# print (beso.name)              #attrubutes/properties
# print (beso.surname)
# print (beso.grade)

# print (beso.say_hello())


# print (jumber.iq)
# print (jumber.name)
# print (jumber.surname)
# print (jumber.grade)

# my_arr = [1, 2, 3, 10]
# print (type(my_arr))

class Cata:
    #iq = 120  #atribute
    def __init__(self, თვალისფერი, სახელი, წონა):  #constractor function
        self.aye_color = თვალისფერი
        self.name = სახელი
        self.weight = წონა
        
        
    def miau(self):
        return "მე მქვია" + self.name
knavila = Cata("მწვანე", "კნავილა", 2)
tetra = Cata("შავი", "თეთრა", 3)
    
print (knavila.miau())
print (knavila.aye_color)
print (knavila.name)
print (knavila.weight)           #attrubutes/properties
print (tetra.miau())
print (tetra.aye_color)
print (tetra.name)
print (tetra.weight)