# # # # # n1 = int(input())
# # # # # n2 = int(input())

# # # # # while n1 <= n2:
# # # # #     if n1 %5 ==0:
# # # # #         break
# # # # #     else:
# # # # #         print("yes")
# # # # #         n1+=1

# # # # for i in range(10):
# # # #     print("it")
# # # n1 = int(input())
# # # n2 = int(input())
# # # for i in range(n1, n2+1, -1):
# # #     if i % 2 ==0 or 1 % 5 ==0:
# # #         print(i)
# # n = int(input())
# # for i in range(1, n+1):
# #     if i%3 == 0 and i%5 == 0:
# #         print("FeezBuzz")
# #     elif i%3 == 0:
# #         print("Feez")
# #     elif i%5 ==0:
# #         print("Buzz")
# #     else:
# #         print(i)

# lst = []
# for i in range(10):
#     n = int(input())
#     lst.append(n)
# print(lst)


lst = []
n = int(input())
for i in range(n+1):
    if n%5 == 0:
        lst.append(i)
        print(lst)