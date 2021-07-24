class Solution:
    def countRecursive(self,array,s,n):
        if s==0:
            return 1
        if n==0 and s!=0:
            return 0
        if array[n-1]>s:
            return self.countRecursive(array,s,n-1)
        else:
            return self.countRecursive(array,s,n-1)+self.countRecursive(array,s-array[n-1],n-1)

    def dpmethod(self,array,sum,n):
        dp=[[None for i in range(0,sum+1)] for j in range(0,n+1)] 
        
        for i in range(0,n+1):
            dp[i][0]=1

        for j in range(1,sum+1):
            dp[0][j]=0

        for i in range(1,n+1):
            for j in range(1,sum+1):
        
                if array[n-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] + dp[i-1][j-array[i-1]]
        return dp[i][j]
s= Solution()
a=[3,1,3,2]
print(s.countRecursive(a,6,len(a)))

print(s.dpmethod(a,6,len(a)))