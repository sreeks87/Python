class A:
    def hello(self):
        print("hello from A")

class B(A):
    def hello(self):
        print("hello from B")
class C(A):
    def hello(self):
        print("hello from C")

class D(C,B):
    pass
    # def hello(self):
    #     print("hello from D")

d=D()
d.hello()