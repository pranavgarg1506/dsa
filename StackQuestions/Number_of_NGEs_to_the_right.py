"""
Need to REVISIT AGAIN
"""


import sys 
import os
from dotenv import load_dotenv
load_dotenv()

BASE_PATH = os.getenv('BASE_PATH')
CUR_PATH = BASE_PATH + '/ds'

sys.path.insert(0, CUR_PATH)

from stack import StackUsingList



arr =[3, 4, 2, 7, 5, 8, 10, 6]
q = 2
indexes = [0,5]

## method1
"""
O(n^2)
"""
for index in indexes:

    if index >= len(arr):
        print("ERROR")
    elif index == len(arr) - 1:
        print(0)
    else:
        count = 0
        for i in range(index+1, len(arr)):
            if arr[i] > arr[index]:
                count += 1

        print(count)

## method2
