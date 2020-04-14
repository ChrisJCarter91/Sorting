import math

# TO-DO: complete the helpe function below to merge 2 sorted arrays

#things to remember:
#Recursive calls itself**

#Merge sorting uses a divide and conquor method.
#Divide in half until you have subarrays of length 1 - a list of len 1 is considered sorted
#Once the lists are sorted, merge them

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):                                                               #Initiate for loop
        if len(arrA) and len(arrB):                                                         # if length of 2 arrays that are sorted 
            if arrA[0] > arrB[0]:                                                           #if the item at 0 index of Array A is greater than the item at 0 index of Array B
                merged_arr[i] = arrB[0]                                                     #The index of the merged_array = the 0 index of array B
                arrB.pop(0)                                                                 #pop the item at index 0 of array B
            else:                                                                           #else
                merged_arr[i] = arrA[0]                                                     #The opposite of lines above. Merged_array index = array A index 0
                arrA.pop(0)                                                                 #pop the item at index 0 of array A
        elif len(arrA):                                                                     #else if the length of array A
            merged_arr[i] = arrA[0]                                                         #index of merged_array = item in 0 position of array A
            arrA.pop(0)                                                                     #pop the item at the 0 index of array A
        elif len(arrB):                                                                     #else if the length of array B
            merged_arr[i] = arrB[0]                                                         #index of merged_array = item in the 0 position of array B
            arrB.pop(0)                                                                     #pop the item at the 0 index of array B

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        arr1 = []
        arr2 = []
        for i in range(0, math.floor(len(arr)/2)):
            arr1.append(arr[i])

        for i in range(math.floor(len(arr)/2), len(arr)):
            arr2.append(arr[i])

        print(arr1)
        print(arr2)
        arr = merge(merge_sort(arr1), merge_sort(arr2))
        print(arr)

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
