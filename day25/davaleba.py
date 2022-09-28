
#Ex.1 (2 points)
# “Write a program that prints the numbers from 1 to n. But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”
#(n is input from the user).”
# Ex: 15 -->
#fizzbuzz
# 1
# 2
# fizz
# 4
# buzz
# fizz
# 7
# 8
# fizz
# buzz
# 11
# fizz
# 13
# 14
# fizzbuzz








n = int(input())

for i in range(1,n+1):
    
    if i%3 and i%5==0:
        
        print("FizzBuzz")
    elif i %3==0:
        print("Fizz")
    elif i %5==0:
        print("Buzz")
    else:
        print(i)
        
        
        

