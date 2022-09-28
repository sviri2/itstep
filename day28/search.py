# arr = [1, 2, 3, 4, 5]

# for i in arr:
#     print(arr)
    
    
    
# O(n)----> n არის სიგრძე

# თუ
# arr =[[1,2,3],[4, 5, 6],[12, 23, 17]]

# for i in arr:
#     for j in i:
#         print(j)
        
# O(n*m)----> n არის სიგრძე m კი შიგა ლისტში არსებული რაოდენობა ელემენტების

# arr1 = [2, 34, 45, 13]

# for i in arr1:
#     for j in i:
#         print(i)
        
# O(n*n)----> n არის სიგრძე და გამოდის რომ კვადრატდება თიტოეული

#search ალგორიტმი______________

# linear_ წრფივი

# lst = [ 10, 12, 45, 1, -23]

# def linear_search(lst, x):
#     for i in lst:
#         if i == x:
#             return True
#         return False
# x = 1
# print(linear_search)




# #binary search --> iterative
# def binary_search(arr,x,low,high):
#     while low <=high:
#         mid = (low+high)//2

 

#         if arr[mid] ==x:
#             return mid

 

#         elif arr[mid] < x:
#             low = mid+1
#         else:
#             high = mid-1

 

#     return -1

 

# #binary search --> recursive
# def binary_search_rec(arr,x,low,high):
#     if high >=low:
#         mid = (low+high)//2

 

#         if arr[mid] ==x:
#             return mid

 

#         elif arr[mid] >x:
#             return binary_search_rec(arr,x,low,mid-1)
#         else:
#             return binary_search_rec(arr,x,mid+1,high)
#     else:
#         return -1


