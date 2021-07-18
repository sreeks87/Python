class Node:
    def __init__(self,d,next=None) -> None:
        self.data=d
        self.next=next


class LinkedList:
    def __init__(self,cap) -> None:
        self.head=None
        self.cap=cap

    def insert(self,data):
        n=DoubleNode(data)
        c=1
        if not self.head:
            self.head=n
            return True
        current=self.head
        while current.next:
            # keep traversing to find the last
            current=current.next
            c+=1
        if c == self.cap:
            self.delete_head()
        current.next=n
        n.previous=current            
        return True
    def delete(self,d):
        current= self.head
        previous=None
        while current:
            if current.data==d:
                print("Deleting {}".format(current.data))
                if previous:
                    previous.next=current.next
                    current.next.previous=previous
                else:
                    self.head=current.next
                break
            previous=current
            current=current.next
    def delete_head(self):
        self.head=self.head.next
        print("Deleting head {}".format(self.head.data))
        if self.head.next:
            self.head.next.previous=None
        
    def findLL(self,d):
        current= self.head
        while current:
            if current.data==d:
                return 1
            current=current.next
        return 0
    def swap(self,d):
        self.delete(d)
        self.insert(d)
        return
    def printLL(self):
        current=self.head
        while current:
            print("Data {}".format(current.data))
            current=current.next

class DoubleNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.previous=None

class LRU:
    def __init__(self,c) -> None:
        self.queue=LinkedList(c)

    def find_in_cache(self,d):
        if self.queue.findLL(d)>0:
            print("Cache hit returning {}".format(d))
            self.queue.swap(d)
            print("Swapped lru with last index")

        else:
            en=self.queue.insert(d)
            # if not en:
            #     print("Cache full, Dq required")
            #     self.queue.delete_head()
            #     self.queue.insert(d)
    
    def printLRU(self):
        self.queue.printLL()

if __name__=='__main__':
    lru=LRU(3)

    lru.find_in_cache(1)
    lru.find_in_cache(2)
    lru.find_in_cache(3)
    lru.find_in_cache(4)
    lru.printLRU()
    print("1------------------")
    lru.find_in_cache(1)
    lru.printLRU()
    print("2------------------")
    lru.find_in_cache(4)
    lru.printLRU()
    print("3------------------")
    lru.find_in_cache(1)
    lru.printLRU()
    print("4------------------")
    lru.find_in_cache(3)
    lru.printLRU()
    print("5------------------")
    lru.find_in_cache(4)
    lru.printLRU()
    print("6------------------")
    lru.find_in_cache(5)
    lru.printLRU()
    print("7------------------")