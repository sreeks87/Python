class Queue:
    def __init__(self,c,array=[]) -> None:
        self.array=array
        self.cap=c

    def enqueue(self,d):
        if(len(self.array)!=self.cap):
            print("ENQ {}".format(d))
            self.array.append(d)
            return True
        else:
            return False

    def dequeue(self):
        print("DQ ")
        self.array.pop(0)
    def printQ(self):
        print(self.array)
    def findQ(self,d):
        if d in self.array:
            return self.array.index(d)
        return -1
    def swap(self,d):
        hitn=self.array.index(d)
        self.array.pop(hitn)
        self.enqueue(d)
class LRU:
    def __init__(self,c) -> None:
        self.queue=Queue(c)

    def find_in_cache(self,d):
        if self.queue.findQ(d)>=0:
            print("Cache hit returning {}".format(d))
            self.queue.swap(d)
            print("Swapped lru with last index")

        else:
            en=self.queue.enqueue(d)
            if not en:
                print("Cache full, Dq required")
                self.queue.dequeue()
                self.queue.enqueue(d)
    
    def printLRU(self):
        self.queue.printQ()

if __name__=='__main__':
    # q=Queue(3)
    # q.enqueue(1)
    # q.enqueue(2)
    # q.enqueue(3)
    # q.printQ()

    # q.dequeue()
    # q.printQ()
    # q.dequeue()
    # q.printQ()

    lru=LRU(3)
    lru.find_in_cache(1)
    lru.find_in_cache(2)
    lru.find_in_cache(3)
    lru.printLRU()

    lru.find_in_cache(1)
    lru.printLRU()
    lru.find_in_cache(4)
    lru.printLRU()
    lru.find_in_cache(1)
    lru.printLRU()
    lru.find_in_cache(3)
    lru.printLRU()
    lru.find_in_cache(4)
    lru.printLRU()
    lru.find_in_cache(5)
    lru.printLRU()
