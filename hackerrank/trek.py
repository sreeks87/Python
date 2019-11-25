def decode_lst(lst):
	int_lst=[-1 if i.lower()=="d" else 1 for i in lst]
	return int_lst


def checkvalley(lst):
	s=0
	m=v=0
	mt=False
	va=False
	for i in lst:
		if i==1 and s==0:
			mt=True
		if i==-1 and s==0:
			va=True	
		s+=i
		if s==0 and va:
			v+=1
			va=False
		if s==0 and mt:
			m+=1
			mt=False
	return v
	
	
inp=input(" Enter the trail -")
inp_lst=inp.replace("[","").replace("]","").split(",")
int_lst=decode_lst(inp_lst)
print(checkvalley(int_lst))



#[d,d,d,u,u,u,d,d,u,u,u,d,d,d,u,u]
#[u,u,d,d,d,u]

