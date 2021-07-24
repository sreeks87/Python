class Solution:
    def knapsack(self,wt_array,pt_array,wt_bag,n):
        #  base condition
        if wt_bag ==0 or n==0:
            return 0
        elif wt_bag<wt_array[n-1]:
            # exclude this
            return self.knapsack(wt_array,pt_array,wt_bag,n-1)
            # return r
        else:
            return max(pt_array[n-1]+self.knapsack(wt_array,pt_array,wt_bag-wt_array[n-1],n-1),self.knapsack(wt_array,pt_array,wt_bag,n-1))


if __name__=='__main__':
    s=Solution()
    wt_array=[10, 20, 30]
    pt_array=[60, 100, 120]
    w=50
    print(s.knapsack(wt_array,pt_array,w,len(pt_array)))

    # complexity=o(2^n) since each element can either be excluded(0) or included(1)