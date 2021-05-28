

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
        self.size = size

    def length(self):
        """
        returns the size of the occupied stack in O(1) Time Complexity
        """
        return self.current_index + 1

    def push(self, ele):
        """
        push the values in the stack in O(1) Time Complexity
        """
        if self.current_index == -1:
            self.current_index += 1
            self.arr[self.current_index] = ele
            return

        if self.size <= self.current_index + 1:
            print("Stack is Full")
        else:
            self.current_index += 1
            self.arr[self.current_index] = ele

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
        if self.length() == self.size:
            return True
        return False

    def pop(self):
        if self.isEmpty():
            print("Stack is already Empty")
            return -1000
        ele = self.arr[self.current_index]
        self.current_index -=1
        return ele





