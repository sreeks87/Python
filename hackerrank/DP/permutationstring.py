

class Solution:
    def permutation(self,a,l,r):
        if l==r:
            print(a)
        for  i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            self.permutation(a,l+1,r)
            a[l],a[i]=a[i],a[l]
    def anotherpermutation(self,a,ret):
        if len(a)==0:
            print(ret)
        for i in range(0,len(a)):
            self.anotherpermutation(a[0:i]+a[i+1:],ret+a[i])

    def subsets(self,a):
        for i in range(len(a)+1):
            for j in range(i,len(a)+1):
                print(a[i:j])
            
s=Solution()
a=list('abc')
s.permutation(a,0,len(a)-1)

# print(ans)
ret=''
s.anotherpermutation(a,ret)

s.subsets('india')



# def subsets(a):
#     for j in range(0,len(a)+1):
#         print(a[0:j])


# subsets('masterstorke')