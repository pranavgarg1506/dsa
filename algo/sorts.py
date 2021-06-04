from ds.linkedlist import LinkedList

def bubbleSort(arr):
    """
    1. Basic Sorting Algorithm
    2. Stable algo.
    3. O(n^2) --> Time Complexity
    Algo:-

    swap the adjancent elements.
    This will take the largest element in every iteration to the last position.

    cons:-
    even if the array is sorted it will keep on checking the adjacent elements.
    """
    n = len(arr)


    for i in range(0,n):

        for j in range(0,n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubbleSort1(arr):

    n = len(arr)

    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if swap == False:
            break

def selectionSort(arr):
    """
    In selection sort, we find the minimum ele from unsorted array part and place it at the beginnning of the array amd keep on doing this.
    ## 8,4,1,6,2,7         1,4,8,6,2,7
    Time Complexity --> O(n^2)
    swaps --> O(n)
    Unstable

    """

    n = len(arr)

    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index],arr[i]

def selectionSortStable(arr):
    n = len(arr)

    for i in range(0,n):
        min_index = i
        for j in range(i,n):
            if arr[j] < arr[min_index]:
                min_index = j

        temp = arr[min_index]
        while min_index > i:
            arr[min_index] = arr[min_index - 1]
            min_index -=1

        arr[i] = temp
