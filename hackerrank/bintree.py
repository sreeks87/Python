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


if __name__=='__main__':
    r=Node()
    r.insert(12)
    r.insert(6)
    r.insert(14)
    r.insert(3)
    r.printTree()



