from ds.stack import Stack
from ds.queue import Queue, CircularQueue

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

q2 = CircularQueue(5)

q2.enQueue(25)
q2.enQueue(26)
e1 = q2.deQueue()
print(e1)
q2.enQueue(39)
q2.printQueue()