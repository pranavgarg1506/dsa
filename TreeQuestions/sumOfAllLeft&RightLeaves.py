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
ans_left = 0
ans_right = 0


def leftLeafRecSum(root, flag):
    global ans_left
    global ans_right
    if root is None:
        return

    if root.left == None and root.right == None:
        if flag == 1:
            ans_left += root.data
        if flag == 2:
            ans_right += root.data

    leftLeafRecSum(root.left, 1 )
    leftLeafRecSum(root.right, 2)

def leftLeafSum(root):
    leftLeafRecSum(root,0)
    return ans_left, ans_right


print(leftLeafSum(t1.root))
