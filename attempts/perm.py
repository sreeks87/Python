print("Permutation")

inp =["a",1,"b",2,"c",3,"d",4]
d={}
for i in range(0,len(inp),2):
   d.update({inp[i]:inp[i+1]}) 
print(d)

d2={inp[i]:inp[i+1] for i in range(0,len(inp),2)}
print(d2)