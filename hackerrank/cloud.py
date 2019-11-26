class CloudGame:
	def __init__(self,n,l):
		self.len=n
		self.cl=l
	def findzero(self):
		l=[]
		for i in range(self.len):
			if self.cl[i]=='0':
				l.append(i)
		return l
		
	def findjumps(self):
		j=0
		i=0
		l=self.findzero()
		while i != l[-1]:
			f=False
			if i+2 in l:
				j+=1
				f=True
				i+=2
			if i+1 in l and not f:
				j+=1
				i+=1
		return j
c=CloudGame(7,list("0010010"))
jm=c.findjumps()
print(jm)
					
					
				
				
			