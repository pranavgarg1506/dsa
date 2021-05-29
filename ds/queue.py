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
            return -1000
        
        ele = self.arr[self.front]
        self.arr[self.front] = -1
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


## CircularQueue using list

class CircularQueue():

    def __init__(self, size):
        """
        Initalizaing the CircularQueue with size 'size'
        """
        self.Q = [-1] * size
        self.rear = self.front = -1
        self.capacity = size
        self.size = 0


    def isEmpty(self):
        if self.rear == -1:
            return True
        return False

    def length(self):
        return self.size

    def isFull(self):
        if self.size == self.capacity:
            return True
        return False

    def enQueue(self, ele):
        if self.isFull():
            print("Queue is already full, cant put any element in it")
            return

        if self.rear == -1:
            self.rear = self.front = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = ele
        self.size += 1

    def deQueue(self):
        if self.isEmpty():
            print("Queue is already Empty")
            return -1000
        
        ele = self.Q[self.front]
        self.Q[self.front] = -1
        self.front = (self.front + 1) % self.capacity
        if (self.front) % self.capacity == (self.rear + 1) % self.capacity:
            self.front = self.rear = 1
        return ele

    def printQueue(self):
        if self.isEmpty():
            print("Queue is already Empty, cannot print anything")
            return
        print("QUEUEUUE")
        for i in range(0, self.capacity):
            print(self.Q[i])

        print("-"*10)