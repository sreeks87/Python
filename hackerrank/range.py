def clean_inp(s):
	st=int(s.split(":")[0].split("[")[1])
	end=int(s.split(":")[1].split("]")[0])
	return[st,end]
	
def is_in_range(lst1,lst2):
	if lst2[0]<lst1[1]:
		return "["+str(lst1[0])+":"+str(lst2[1])+"]"
	else:
		return ""

inp=input("enter the list-")
user=inp[1:-1].split(",")
tmp_lst=[0,0]
op_lst=[]
for i in user:
	clean_lst=clean_inp(i)
	is_range=is_in_range(tmp_lst,clean_lst)
	if is_range!="":
		op_lst.append(is_range)
	tmp_lst=clean_lst
	
print(op_lst)



