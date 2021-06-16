"""
1. 

"""


arr = [8,77,4,1,6,2,7,-8]
n = len(arr)

for i in range(1,n):
    temp = arr[i]

    j = i -1
    while j >= 0 and arr[j] > temp:
        arr[j+1] = arr[j]
        j -=1
    arr[j+1] = temp

print(arr)