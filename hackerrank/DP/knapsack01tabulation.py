class Solution:
    def knapsack(self,wt_array,pt_array,wt_bag,n):
        #  base condition
        # dp=[[0]*wt_bag]*n 
        dp=[[None for i in range(0,wt_bag)] for j in range(0,n)] 
        for i in range(0,n):
            for j in range(0,wt_bag):
                if i==0 or j==0:
                    dp[i][j]=0
                elif wt_array[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    # the new value will be a max of elif case->exclude when wight of item>current capacity of bag
                    # and the included case -> add the profit to the current cell with the previous cell of capacity, because now capacity decreased
                    dp[i][j]=max(dp[i-1][j], pt_array[i-1]+dp[i-1][wt_bag-wt_array[i-1]])

        for i in range(0,n):
            for j in range(0,wt_bag):
                print(dp[i][j],end=' ')
            print()
        return dp[i][j]

        # if wt_bag ==0 or n==0:
        #     return 0
        # elif wt_bag<wt_array[n-1]:
        #     # exclude this
        #     return self.knapsack(wt_array,pt_array,wt_bag,n-1)
        #     # return r
        # else:
        #     return max(pt_array[n-1]+self.knapsack(wt_array,pt_array,wt_bag-wt_array[n-1],n-1),self.knapsack(wt_array,pt_array,wt_bag,n-1))


if __name__=='__main__':
    s=Solution()
    wt_array=[1, 4, 3]
    pt_array=[2, 4, 4]
    w=5
    print(s.knapsack(wt_array,pt_array,w,len(pt_array)))

    # complexity=o(2^n) since each element can either be excluded(0) or included(1)