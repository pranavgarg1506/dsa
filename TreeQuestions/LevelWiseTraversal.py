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

def printLevelWiseTraversal(root):
    if root is None:
        return

    q1 = []

    q1.append(root)

    while len(q1) > 0:
        print(q1[0].data)

        temp = q1.pop(0)

        if temp.left is not None:
            q1.append(temp.left)

        if temp.right is not None:
            q1.append(temp.right)


printLevelWiseTraversal(t1.root)