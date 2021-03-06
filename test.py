from ds.stack import Stack, StackUsingList
from ds.queue import Queue, CircularQueue
from ds.linkedlist import LinkedList
from ds.tree import BinarySearchTree
from algo.sorts import bubbleSort, mergeSort, selectionSort, selectionSortStable, bubbleSort2,insertionSort


"""s1 = Stack(2)
print(s1.length())
s1.push(125)
s1.printstack()
s1.push(236)
s1.printstack()
s1.push(33)
print(s1.isEmpty())
print(s1.isFull())"""



## this chunk is for the implementation of Lineara queue
"""q1 = Queue(3)

print(q1.length())
q1.enQueue(6)
q1.enQueue(23)
q1.printQueue()
print(q1.length())
ans = q1.deQueue()
print("ans",ans)
q1.printQueue()
"""

## tests for Circular Queue
"""q2 = CircularQueue(5)

q2.enQueue(25)
q2.enQueue(26)
e1 = q2.deQueue()
print(e1)
q2.enQueue(39)
q2.printQueue()"""
"""
ll1 = LinkedList()

ll1.insertAtFirst(5)
ll1.insertAtEnd(8)
ll1.insertAtEnd(11)
ll1.insertAtPos(3, 36)
ll1.printLL()
"""

"""tree = BinarySearchTree()
arr = [3,6,1,8,2,9,11,67]
for i in arr:
    tree.create(i)

pre = tree.preOrderTraversal(tree.root)
inn = tree.inOrderTraversal(tree.root)
post = tree.postOrderTraversal(tree.root)

print(*pre, sep=' ', end="\n")
print(*inn, sep=' ', end="\n")
print(*post, sep=' ', end="\n")
"""

"""
arr = [6,5,4,12,3,2,1]
mergeSort(arr)
print(arr)
"""

s = StackUsingList()
s.push(5)
s.push(44)
s.push(11)
s.printStack()