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

def bubbleSort2(arr):
    """
    using single while loop
    """
    n = len(arr)
    nop = 0
    i = 0
    j = 1

    while nop < n:
        if j == n:
            i = 0
            j = 1
            nop+=1
        else:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j],arr[i]
            i += 1
            j += 1


def selectionSort(arr):
    """
    In selection sort, we find the minimum ele from unsorted array part and place it at the beginnning of the array amd keep on doing this.
    ## 8,4,1,6,2,7         1,4,8,6,2,7
    Time Complexity --> O(n^2)
    swaps --> O(n)
    Unstable
    This is efficient when memory writing is very costly.

    """
    n = len(arr)

    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j

        ## swap part
        arr[i], arr[min_index] = arr[min_index], arr[i]


def selectionSortStable(arr):
    n = len(arr)

    for i in range(0,n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        ## making it stable
        temp = arr[min_index]
        while min_index > i:
            arr[min_index] = arr[min_index - 1]
            min_index -=1
        arr[i] = temp
        

def insertionSort(arr):
    n = len(arr)

    for i in range(1,n):

        temp = arr[i]
        j = i-1
        while j >=0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = temp


def mergeSort(arr):
    """
    Recursive Solution for merge sort
    """

    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                arr[k] = right[j]
                j += 1
            else:
                arr[k] = left[i]
                i += 1
            k +=1

        ## if any of the left or right array is left empty then

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

            

