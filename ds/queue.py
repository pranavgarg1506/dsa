## rear addition
## front deletion

## Implementation using List

class Queue():


    def __init__(self, size):
        self.arr = [-1] * size
        self.rear = self.front = -1
        self.capacity = size

    def isFull(self):
        if self.rear == -1:
            return False
        
        if self.rear == self.capacity - 1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.rear == -1:
            return True

        return False

    def enQueue(self, ele):
        if self.isFull():
            print("Queue is already Full")
            return 
        
        ## addition of first element
        if self.rear == -1:
            self.rear = self.front = 0
            self.arr[self.rear] = ele
        else:
            self.rear += 1
            self.arr[self.rear] = ele

    def deQueue(self):
        if self.isEmpty():
            print("Queue is already Empty, nothing to remove")
            return
        
        ele = self.arr[self.front]
        self.front += 1
        if self.front > self.rear:
            self.front = self.rear = -1
        return ele

    def printQueue(self):
        if self.isEmpty():
            print("Queue is already Empty, cannot print anything")
            return
        
        for i in range(self.front, self.rear+1):
            print(self.arr[i])

        print("-"*10)

    def length(self):
        if self.isEmpty():
            return 0

        return self.rear - self.front + 1
