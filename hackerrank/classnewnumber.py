class NewNumber:
    def __init__(self,n=0):
        self.n=n
    
    def finddouble(self):
        return self.n*self.n
    @property
    def n(self):
        print("Getting..")
        return self._n

    @n.setter
    def n(self,n):
        print("Setting..")
        if(n<100):
            raise ValueError("Error..")
        self._n=n
try:
    num=NewNumber(99)
    print(num.finddouble())
    import array
    s= array.array('a',[1,2,3])
except ValueError as v:
    print("Value error "+str(v))
else:
    print("Some other exception occured!!!")
finally:
    print("I am done!!!")





