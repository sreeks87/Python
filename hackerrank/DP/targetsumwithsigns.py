# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.dpmethod(nums,target,len(nums))

    def dpmethod(self,array,s,n):
        dp=[[None for i in range(0,s+1)]for j in range(0,n+1)]

        for i in range(0,n+1):
            dp[i][0]=1
        for j in range(1,s+1):
            dp[0][j]=0

        for i in range(1,n+1):
            for j in range(1,s+1):
                if array[n-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j] + dp[i-1][j-array[i-1]]
        return dp[i][j]

a=[1,1,1,1,1]
su=3
s=Solution()
print(s.findTargetSumWays(a,3))