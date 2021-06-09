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


## checking the number of nodes and their sum
INTERNAL_NODES = 0
LEAF_NODES = 0
NODES_SUM = 0

def Summary(root):
    global INTERNAL_NODES
    global LEAF_NODES
    global NODES_SUM
    if root is None:
        return

    if root.left == None and root.right == None:
        LEAF_NODES += 1
        NODES_SUM += root.data
        return
    
    INTERNAL_NODES += 1
    NODES_SUM += root.data

    if root.left:
        Summary(root.left)

    if root.right:
        Summary(root.right)



Summary(t1.root)
print("SUMMARY of the Tree:-\n")
print("Internal Nodes:-",INTERNAL_NODES)
print("Leaf Nodes:-",LEAF_NODES)
print("Sum is:-",NODES_SUM)
