class sock:
	def __init__(self,n,l):
		self.tot=n
		self.sl=l
		
	def findsock(self):
		d={}
		for i in self.sl:
			if i in d:
				d[i]=d[i]+1
			else:
				d[i]=1
		lst=[int(v/2) for k,v in d.items() if int(v/2)>0]
		r=sum(lst)
		return r
		
sk=sock(9,[10,20,20,10,10,30,50,10,20])
print(sk.findsock())