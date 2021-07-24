class Solution:
    def knapsack(self,wt_array,pt_array,wt_bag,n):
        #  base condition
        mem=[[-1]*wt_bag]*n 
        if wt_bag ==0 or n==0:
            return 0
        # lookup, if the SP was already computed or not if yes , return.
        if mem[n-1][wt_bag-1]== -1:
            if wt_bag<wt_array[n-1]:
                # exclude this
                mem[n-1][wt_bag-1]= self.knapsack(wt_array,pt_array,wt_bag,n-1)
                # return r
            else:
                mem[n-1][wt_bag-1]= max(pt_array[n-1]+self.knapsack(wt_array,pt_array,wt_bag-wt_array[n-1],n-1),self.knapsack(wt_array,pt_array,wt_bag,n-1))
        # return since already computed
        return mem[n-1][wt_bag-1]

if __name__=='__main__':
    s=Solution()
    wt_array=[1, 4, 3]
    pt_array=[2, 4, 4]
    w=5
    print(s.knapsack(wt_array,pt_array,w,len(pt_array)))

    # complexity=o(n*w) 