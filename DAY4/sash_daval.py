# #შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რამე სტრინგი
# #დაითვლის ამ სტრინგში ასო "i"ს რაოდენობას და დააბრუნებს რიცხვად ამ მნიშვნელობას

# def i_rao(name):
#     raodenoba = name.count("i")
#     return raodenoba

# print(i_rao("besiki"))





# #შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რაღაც რიცხვი
# #დააბრუნოს მნიშვნელობად 1-იდან ამ რიცხვამდე რიცხვების ჯამი.
# #მაგალითად 4 -->   1+2+3+4 = 10



# def ricxvi(n):
#      my_sum = 0 
#      for element in range(n):
#            my_sum += element
#      return my_sum


# x = int(input("შეიყვანეტ საჭირო რიცხვი: "))

# print(ricxi(x))

def solution(string):
    reversed_word = ""
    
    for i in range(len(string)):
        reversed_word += string[i*-1 -1]
    
    
    
print(solution("beso")) 
    