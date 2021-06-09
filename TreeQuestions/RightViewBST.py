import sys 
import os
from dotenv import load_dotenv
load_dotenv()

BASE_PATH = os.getenv('BASE_PATH')
CUR_PATH = BASE_PATH + '/ds'

sys.path.insert(0, CUR_PATH)
from tree import BinarySearchTree

## method 1 
## using queue

t1 = BinarySearchTree()
t1.create(25)
t1.create(45)
t1.create(5)
t1.create(4)
t1.create(15)
t1.create(95)
t1.create(75)
t1.create(56)
t1.create(61)
t1.create(59)

"""
                                25
                    5                           45
                4       15                            95
                                                75
                                            56
                                                61
                                            59
"""

def RightViewOfBST(root):
    if root is None:
        return

    q1 = []

    q1.append(root)

    while len(q1) > 0:
        n = len(q1)

        for i in range(1,n+1):
            temp = q1[0]
            q1.pop(0)

            ## print 1st element
            if i == n:
                print(temp.data)

            if temp.left is not None:
                q1.append(temp.left)

            if temp.right is not None:
                q1.append(temp.right)

RightViewOfBST(t1.root)