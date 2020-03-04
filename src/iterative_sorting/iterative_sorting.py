# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(len(arr)  -1  , 0 ,-1):
        # print(i)
        for x in range(0, i ): # this is the second number (index)
            if arr[x] > arr[i]:
                arr[i],arr[x] = arr[x],arr[i] # we swap the biggest to the left index
    print(arr)
    # if(arr[-1] < arr[0]):
    #     arr[-1], arr[0] = arr[0], arr[-1]
    # print((arr))

    return arr


selection_sort([2,4,6,1,2,3,4,8,10])
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr) - 1):
        for x in range(i + 1, len(arr)):  # this is the second number (index)
            if arr[i] > arr[x]:
                arr[i], arr[x] = arr[x], arr[i]

    return arr
#
#
# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):
#
#     return arr