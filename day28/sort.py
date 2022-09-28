# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):

 

#             if arr[j] >arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr
 
 
 
#selection sort
# [7, 2, 1, 6]---> [1, 7, 3 ,6]--->[1, 2, 7, 6]--->[1, 2, 6, 7]


from re import A


def selection_sort(arr):
    size = len(arr)
    for i in range(size):
        min_ind = i
        
        for j in range(i+1, size):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i],arr[min_ind] = arr[min_ind],arr[i]
        
    return arr
        
        
        
    
print(selection_sort([7, 2, 1, 6]))

#insertion sort
[7, 2, 1, 6] ---> [2, 7, 1, 6] ---> [2, 1, 7, 6]--->[1, 2, 7, 6]--->[1, 2, 6, 7]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        a = arr[1]
        j = i - 1
        
        while j >= 0 and a < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j-1] = a
    return arr
        
    
    
