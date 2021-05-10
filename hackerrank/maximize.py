def maximize(l,m):
    sum=0
    for i in l:
        sum+=max(i)**2
    return sum%m


k,m=map(int,input().split(" "))
l=[]
for i in range(k):
    l.append(list(map(int,input().split(" "))))

print(maximize(l,m))

