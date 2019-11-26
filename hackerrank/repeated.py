class Repeat:
    def __init__(self,s,n):
        self.str=s
        self.l=n
    
    def count_a(self,str):
        c=0
        for i in str:
            if i=='a':
                c+=1
        return c

    def repeatedString(self):
        sl=len(self.str)
        c=self.count_a(self.str)
        mod=self.l%sl
        if mod==0:
            return int(self.l/sl)*c
        else:
            return int(self.l/sl)*c + self.count_a(self.str[:mod])

r=Repeat('abab',100)
print(r.repeatedString())



