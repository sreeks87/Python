def isAnagram(a,b):
    c=0
    for i in a:
        if i in (b):
            c+=1
    if c== len(a):
        return True
    else:
        return False


list = ["ate","cat","tea","bat","nat","tan","ant"]
d={}
for i in range(len(list)-1):
    l=[]
    for j in range(i+1,len(list)):
        if isAnagram(list[i],list[j]):
            l.append(list[j])
            d[list[i]]=l
print(d)