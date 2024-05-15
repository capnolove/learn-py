class Node:
    def __init__ (self, data) :
        self.left=None
        self.right=None
        self.data=data

    # insert node to tree
    def insert (self, data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            if data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)

    # print tree with in ordered traversal
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    # add node by in order traversal to list
    def inOrderTraversal(self, root):
        tree=[]
        if root:
            res=self.inOrderTraversal(root.left)
            res.append(root.data)
            res=res+self.inOrderTraversal(root.right)
            return res
        
    # add node by post order traversal to list
    def postOrderTraversal(self, root):
        tree=[]
        if root:
            res=self.inOrderTraversal(root.left)
            res=res+self.inOrderTraversal(root.right)
            res.append(root.data)
            return res
    

root=Node(input())
root.insert(input())
root.insert(input())
root.insert(input())
root.insert(input())
root.insert(input())
root.printTree()