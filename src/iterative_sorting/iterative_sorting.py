# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):                  #selection_sort takes in an array, i is the index starting at the 0 index and running through the length of the array -1 which would be the last indexed item
        cur_index = i                                 #the current index we are on is represented with i
        smallest_index = cur_index                    #Looking for the smallest index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i+1, len(arr)):                #for each item (x) in the array with a range of index +1 through length of the array
            if arr[smallest_index] > arr[x]:          #if the smallest index of the array is > array x:
                smallest_index = x                    #the smallest index goes to array x



        # TO-DO: swap
        arr[cur_index], arr[smallest_index] =\
        arr[smallest_index], arr[cur_index]




    return arr


# TO-DO:  implement the Bubble Sort function below

#Bubble sorting takes 2 items in the array and compares them and swaps them right to left if the left is greater than the right. 
#If a number pair "bubbles" then the entire array must be gone through again

def bubble_sort( arr ):
    swap = True                                       #boolean
    while swap == True:                               #While boolean is true
        swap = False                                  #boolean is false
        for i in range(len(arr)-1):                   #for each indexed item in the array that's in the range of the length of the array -1 (last indexed item of the array)
            if arr[i] > arr[i+1]:                     #if the indexed item of the array is > the indexed item +1
                arr[i], arr[i+1] = arr [i+1], arr[i]  #We are swapping the indexed item and the indexed item +1
                swap = True                           #boolean is true

    return arr

test_array = [8, 7, 2, 5, 1, 9, 4, 3, 6]
print(test_array)
#test_array = selection_sort(test_array)
test_array = bubble_sort(test_array)
print(test_array)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr