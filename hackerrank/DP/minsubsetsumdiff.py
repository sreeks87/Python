# minumum subst sum difference
import math
from abc import abstractproperty


class Solution:
    def formDP(self,arr):
        n=len(arr)
        sa=sum(arr)
        s=math.ceil(sa//2)

        resarray= self.dpmethod(arr,sa,n)
        d=math.inf
        for i in range(0,s+1):
            if resarray[n][i]:
                d2=sa-2*i
                if d2<d:
                    d=d2
        print("The minimum difference is {}".format(d))
    
    def dpmethod(self,arr,sum,n):
        dp=[[None for i in range(0,sum+1)] for j in range(0,n+1)]

        for i in range(0,n+1):
            dp[i][0]=True

        for j in range(1,sum+1):
            dp[0][j]=False

        for i in range(1,n+1):
            for j in range(1,sum+1):
                if j<arr[n-1]:
                    dp[i][j]=dp[i-1][j]
                if j>=arr[i-1]:
                    dp[i][j]=(dp[i-1][j] or dp[i-1][j-arr[i-1]])

    
        return dp

s= Solution()
a=[2,4,2,3]

s.formDP(a)