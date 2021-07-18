class Node:
    def __init__(self,d,next=None) -> None:
        self.data=d
        self.next=next


class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def insert(self,data):
        n=Node(data)
        current=self.head
        if current:
            while current.next:
                current=current.next
            current.next=n
        else:
            self.head=n 

    def delete(self,d):
        current= self.head
        previous=None
        while current:
            if current.data==d:
                print("Deleting {}".format(current.data))
                if previous:
                    previous.next=current.next
                break
            previous=current
            current=current.next
    def printLL(self):
        current=self.head
        while current:
            print("Data {}".format(current.data))
            current=current.next


if __name__=='__main__':
    l=LinkedList()
    l.insert(1)
    l.insert(2)
    l.insert(3)

    l.printLL()
    l.delete(2)
    l.printLL()
