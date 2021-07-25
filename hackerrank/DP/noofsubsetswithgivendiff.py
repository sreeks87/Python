# number of subsets with given difference
# Given an integer array A containing N integers.
# You need to divide the array A into two subsets S1 and S2 such that the absolute difference between their sums is minimum.
class Solution:

    def dpmethod(self,array,sum,n):

        dp=[[None for i in range(0,sum+1)]for j in range(0,n+1)]

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

    

a=[3,1,2,3]
diff=3
s=sum(a)

s1=(s+diff)//2
s=Solution()
print(s.dpmethod(a,s1,len(a)))

