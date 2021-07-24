# recursions

class Recursion:

    def sum_of_numbers(self,n):
        # base condition
        if n==1:
            return 1
        else:
            return n+ self.sum_of_numbers(n-1)

    def fact(self,n):
        # base condition
        if n==1:
            return 1
        else:
            return n*self.fact(n-1)

    def fib(self,n):
        # base condition
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)

    def reverseString(self,s):
        # base condition, if last element return element
        if len(s)==1: 
            return s
        else:
            return self.reverseString(s[1:])+s[0]

r=Recursion()
print(r.sum_of_numbers(5))
print(r.fact(50))
for i in range(5):
    print(r.fib(i))
print(r.fib(8))

print(r.reverseString('1234'))
# s=reversed('look forward')
# print('-------------------')
# for i in s:
#     print(i,end='')

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return
        while head and head.next:
            head.val,head.next.val=head.next.val,head.val
            head = head.next.next


        
h=ListNode(val=10)
h2=ListNode(val=20)
h3=ListNode(val=30)
h4=ListNode(val=40)
h.next=h2
h2.next=h3
h3.next=h4

s=Solution()
s.swapPairs(h)
while h:
    print(h.val)
    h=h.next
