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

r=Recursion()
print(r.sum_of_numbers(5))
print(r.fact(50))
for i in range(5):
    print(r.fib(i))
print(r.fib(8))