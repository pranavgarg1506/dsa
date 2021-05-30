

## implementation using list
class Stack():

    def __init__(self, size):
        """
        Initalizing the stack with the size
        """
        if size < 1:
            print("Size of stack should be greater than 0")
            return
        self.arr = [-1] * size
        self.current_index= -1
        self.capacity = size
        self.size = 0

    def length(self):
        """
        returns the size of the occupied stack in O(1) Time Complexity
        """
        return self.size

    def push(self, ele):
        """
        push the values in the stack in O(1) Time Complexity
        """
        if self.current_index == -1:
            self.current_index = 0
            self.arr[self.current_index] = ele
            self.size = 1
            return

        if self.capacity <= self.length():
            print("Stack is Full")
        else:
            self.current_index += 1
            self.arr[self.current_index] = ele
            self.size += 1

    def printstack(self):
        print("Printing Stack")

        for i in range(0,self.length()):
            print(self.arr[i])
        print("-"*10)

    def isEmpty(self):
        if self.length() == 0:
            return True
        return False

    def isFull(self):
        if self.length() == self.capacity:
            return True
        return False

    def pop(self):
        if self.isEmpty():
            print("Stack is already Empty")
            return None
        ele = self.arr[self.current_index]
        self.current_index -=1
        return ele

    def top(self):
        if self.isEmpty():
            return None
        return self.arr[self.current_index]




