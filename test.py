class Node:

    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

node =Node(4)    
node.left=Node(3)
node.right=Node(5)
node.left.left=Node(6)

