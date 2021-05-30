class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList():

    def __init__(self) -> None:
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def insertAtFirst(self, data):
        temp_node = Node(data)

        ## if LL is empty then 
        if self.isEmpty():
            self.head = temp_node
            return

        ll = self.head
        self.head = temp_node
        temp_node.next = ll
        return

    def insertAtEnd(self, data):
        temp_node = Node(data)

        ll = self.head
        while ll.next != None:
            ll = ll.next

        ll.next = temp_node

    def insertAtPos(self, pos, data):
        temp_node = Node(data)

        ## position is counted from the staring and no position such as 0 is considered.
        ll = self.head
        print(ll.data)
        count = 1
        while pos-1 > count:
            ll = ll.next
            print("in loop",ll.data)
            count += 1
        print(ll.data)
        temp_node.next = ll.next
        ll.next = temp_node
        return

    def printLL(self):
        ll = self.head
        print("HEAD", "--> ", end="")
        while ll.next != None:
            print(ll.data, "--> ", end='')
            ll = ll.next
        print(ll.data)

    



        



        

        
