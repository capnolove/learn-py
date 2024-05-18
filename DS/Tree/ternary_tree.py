class Node:
    def __init__(self, data, isLeaf=False):
        self.data=data     
        self.left=None     
        self.equal=None    # middle child (equal to data)
        self.right=None    
        self.isLeaf=False

def insert(root, word):
    if not root:    # if "root" is None (empty tree), create new node as 1st char of "word" and set it "root"
        root=Node(word[0])
    if word[0]<root.data:                           
        root.left=insert(root.left, word)
    elif word[0]>root.data:
        root.right=insert(root.right,word)
    else:
        if len(word)>1:    # if not traversed (len(word)>1 or more char to insert)  
            root.equal=insert(root.equal, word[1:])    #  insert the whole word after removing the first character (word[1:])
        else:    # if traversed (len(word)==1 or last char)
            root.isLeaf=True    # set isLeaf to this root for marking this one completed
    return root