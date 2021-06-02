"""
Concepts:-

1. N(root nodes) + N(internal nodes) = Toatal number of nodes
2. Recursive Data Structure

3. height of a node is measured form the base, conside it as maximum possible height from the base line.
4. hegiht of all leaf nodes are 0.

5. depth is taken as reference from the root.
6. depth of root is 0.

7. level = Depth + 1


Traversals in Binary Tree
Pre Order    Node Left Right
Inorder      Left Node Right
Post Order   Left Right Node

Level Order Traversal

"""
class Node:

    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None

    def create(self, data):
        ## checking for the root

        if self.root == None:
            self.root = Node(data)
        else:
            curr = self.root
            temp_node = Node(data)

            while True:
                if data < curr.data:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = temp_node
                        break
                elif data > curr.data:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = temp_node
                        break
                else:
                    break

    ## All traversal using recursion
    def preOrderTraversal(self, root):
        if root == None:
            return
        print(root.data, end=" ")
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)


    def inOrderTraversal(self, root):
        if root == None:
            return
        self.inOrderTraversal(root.left)
        print(root.data, end = " ")
        self.inOrderTraversal(root.right)

    def postOrderTraversal(self, root):
        if root == None:
            return

        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print(root.data, end=" ")




    
