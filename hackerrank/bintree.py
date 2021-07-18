class Node:
    def __init__(self,d) -> None:
        self.right=None
        self.left=None
        self.data=d
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    def insert(self,d):
            if self.data:
                if d<self.data: 
                    if self.left==None:
                        self.left=Node(d)
                    else:
                        self.left.insert(d)
                elif d>self.data:
                    if self.right==None:
                        self.right=Node(d)      
                    else:
                        self.right.insert(d)      
            else:
                self.data=d
    def inOrder(self,vals):
        if self.left is not None:
            self.left.inOrder(vals)
        if self.data is not None:
            vals.append(self.data)
        if self.right is not None:
            self.right.inOrder(vals)
        print(vals)
    def preOrder(self,vals):
        if self.data is not None:
            vals.append(self.data)
        if self.left is not None:
            self.left.preOrder(vals)
        if self.right is not None:
            self.right.preOrder(vals)
        print(vals)
    def postOrder(self,vals):
        if self.left is not None:
            self.left.postOrder(vals)
        if self.right is not None:
            self.right.postOrder(vals)
        if self.data is not None:
            vals.append(self.data)
        print(vals)
if __name__=='__main__':
    r=Node(12)
    r.insert(6)
    r.insert(14)
    r.insert(3)
    r.printTree()
    print("---------ordering-------------")
    r.inOrder([])
    print("---------------------")
    r.preOrder([])
    print("----------------------")
    r.postOrder([])
    print("-------------------")



