class sock:
	def __init__(self,n,l):
		self.tot=n
		self.sl=l
		
	def findsock(self):
		c=1
		d={}
		for i in self.sl:
			if i in d:
				d[i]=c+1
			else:
				d[i]=c
		return [k for k,v in d.items() if v%2==0]
		
sk=sock(4,[1,1,2,3])
print(sk.findsock())