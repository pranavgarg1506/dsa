## Very Basic and Simplest Algo.
## In every pass we compare the adjacent numbers and this will take the maximum number at the end.
## Stable sorting Algo. --> Relative order would be same.
## In Sort Algo --> No extra space is needed.

arr = [4,7,1,9,2,16,14]
n = len(arr)

## method 1
for i in range(0, n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("METHOD 1",arr)

## method 2
## if no swap happened in the pass then break the loop

isSwaped = False
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1][j]
            isSwaped = True

    if isSwaped == False:
        break

print("METHOD 2",arr)


"""
1. If arr is sorted then it will take only 1 pass and then array will be sorted.
2. O(n), O(n^2), O(n^2)
"""





