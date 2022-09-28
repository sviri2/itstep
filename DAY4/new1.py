# name = input("enter your name:")
# surname = input("enter your surname:")

# print(name, surname)

# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))
# print(num1 + num2)

age = input("enter your age: ")
name = input("enter your name: ")
surname = input ("enter your surname: ")
my_text = "hi {} your surname {} is and your age is {}"
print(my_text.format(name, surname, age))