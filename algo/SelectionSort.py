"""
1. It finds the least elememt from the array and swap it with the first index element.
2. In sort algo
3. Not Stable
"""

arr = [8,77,4,1,6,2,7,-8]
n = len(arr)

## method 1(Unstable Sort)
for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[min_index], arr[i] = arr[i], arr[min_index]

print(arr)

## method 2 (making it stable)

for i in range(n):
    min_index = i

    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    ## swapping
    temp = arr[min_index]

    while min_index > i:
        arr[min_index] = arr[min_index-1]
        min_index -=1

    arr[i] = temp

print(arr)