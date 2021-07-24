# subsetsum.py

class Solution:
    def backTrackingRecusrsion(self,array,sum,n):
        # we reduced the sum in every step while including an element, so finally the sum ==0 means, we have found the elements that can make up sum
        if sum==0:return True
        # we kept reducing the sum and going n-1 the elements, now w ehave exhausted all the elements but still nothing could make up a sum. so False
        if n==0 and sum!=0:return False
        if array[n-1]>sum:
            return self.backTrackingRecusrsion(array,n-1,sum)
        else:
            return self.backTrackingRecusrsion(array,sum,n-1) or self.backTrackingRecusrsion(array,sum-array[n-1],n-1)

    def dpmethod(self,array,sum,n):
        dp=[[None for i in range(0,sum+1)] for j in range(0,n+1)] 
        
        for i in range(0,n+1):
            dp[i][0]=True

        for j in range(1,sum+1):
            dp[0][j]=False

        for i in range(1,n+1):
            for j in range(1,sum+1):
                if j<array[n-1]:
                    dp[i][j]=dp[i-1][j]
                if j>=array[i-1]:
                    dp[i][j]=(dp[i-1][j] or dp[i-1][j-array[i-1]])
        return dp[n][sum]

s= Solution()
print(s.backTrackingRecusrsion([1,2,3],8,3))
print(s.dpmethod([1,2,3],8,3))