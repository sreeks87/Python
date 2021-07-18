class Node:

    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    
    def __init__(self):
        self.head=None
    def printList(self):
        h=self.head
        while h:
            print("Data = {0}".format(h.data))
            h=h.next
    def printReverse(self):
        h=self.head
        while h:
            if h.next:
                h=h.next
            else:
                print("Reversed data {0}".format(h.data))     
                h=h.previous   
                while h:
                    print("Reversed data {0}".format(h.data)) 
                    h=h.previous

class DoubleNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.previous=None

if __name__=='__main__':
    ll=LinkedList()

    
    node1=DoubleNode(1)
    ll.head=node1
    node2=DoubleNode(2)
    node3=DoubleNode(3)

    node1.next=node2
    node2.next=node3
    node2.previous=node1
    node3.previous=node2
    ll.printList()

    ll.printReverse()