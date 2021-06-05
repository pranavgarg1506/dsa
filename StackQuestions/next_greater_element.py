## https://www.geeksforgeeks.org/next-greater-element/

# example [4,5,2,25]  -->  [5,25,25,-1]
import sys 
import os
from dotenv import load_dotenv
load_dotenv()

BASE_PATH = os.getenv('BASE_PATH')
CUR_PATH = BASE_PATH + '/ds'

sys.path.insert(0, CUR_PATH)

from stack import StackUsingList



## method 1 
## brute force
## O(n^2)
arr = [4,5,2,25]

for i in range(0, len(arr)):
    found = False

    for j in range(i+1, len(arr)):

        if arr[j] > arr[i]:
            arr[i] = arr[j]
            found = True
            break
    if found == False:
        arr[i] = -1

##print(arr)



## method 2
## using stack
# example [67,4,1,2,25]  -->  [-1,25,2,25,-1]

s = StackUsingList()
arr = [60,67,4,1,2,25]
arr1 = [0] * len(arr)

for i in range( len(arr) - 1, -1, -1):
    
    while (s.isEmpty() == False) and (s.peep() <= arr[i]):
        s.pop()
    
    
    ## if stack is empty
    if s.isEmpty():
        arr1[i] = -1
    else:
        arr1[i] = s.peep()

    s.push(arr[i])
    print("END OF EACH STEP")
    s.printStack()

print(arr1)