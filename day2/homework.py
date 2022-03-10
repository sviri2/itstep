name = input("enter your name: ")
surname = input("enter your surname: ")
grade = int(input("enter your grade: "))
x = int(name.count("i"))
y = str(surname[-6:])
a = ("თქვენ მოიგეთ,  სახელი {} გვარი {} თქვენი ქულაა {} ")
b = ("თქვენ წააგეთ,  სახელი {} გვარი {} თქვენი ქულაა {} ")
if(grade > 50 and x > 1 and y == "shvili" ):

   print(a.format(name, surname, grade))
else:
    print(b.format(name, surname, grade))