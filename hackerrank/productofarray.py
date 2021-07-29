from typing import List
class Solution:
    loop=0
    def productExceptSelfWorst(self, nums: List[int]) -> List[int]:
        self.loop=0
        r=[]
        p=1
        for i in range(len(nums)):
            self.loop+=1
            p=self.pdt(nums[0:i])*self.pdt(nums[i+1:])
            r.append(p)
        # print(self.loop)
        return r
    def pdt(self,n):
        p=1
        for i in n:
            self.loop+=1
            p*=i
        return p
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=[1 for _ in range(len(nums))]
        p=1
        for i in range(len(nums)):
            if i==0:
                p=nums[i]
            else:    
                p*=nums[i]
            left.append(p)
        # print(left)
        p=1
        l=len(nums)-1
        for j in range(len(nums)):
            if l==l-j:
                p=nums[l-j]
            else:    
                p*=nums[l-j]
            right[l-j]=p
        # print(right)
        res=[]
        for k in range(len(nums)):
            if k ==0:
                res.append(right[k+1])
            elif k==l:
                res.append(left[k-1])
            else:
                res.append(left[k-1]*right[k+1])
        # print(res)
        return res
s= Solution()
a= [-1,1,0,-3,3]
# complexity = O(n2)
print(s.productExceptSelf(a))
arr = [10, 3, 5, 6, 2] 
print(s.productExceptSelf(arr))
