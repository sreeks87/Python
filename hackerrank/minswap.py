#!/bin/python3

import math
import os
import random
import re
import sys


class MinSwap:
    def __init__(self,n,arr):
        self.n=n
        self.arr=arr

# Complete the minimumSwaps function below.
    def minimumSwaps(self):
        moved=0
        # diff=0
        # swap=False
        # for i in range(1,self.n+1):
            # diff=q[i-1]-i
            # if diff >0:
            #     # s=s+diff
            #     if diff>2:
            #         return 'Too chaotic'

        for _ in range(self.n):
            m=max(self.arr)
            self.arr.pop(self.arr.index(m))
            print(m)
            # diff=self.arr[i]-(i+1)
            # # if diff>2:
            # #     return 'Too chaotic'
            # if diff >0:
            # # s=s+diff
            #     if diff>2:
            #         return 'Too chaotic'
            # if i+1 != self.arr[i]:
            #     # do bubble
            # for j in range(i+1,n):
            #     if self.arr[i]>self.arr[j]: 
            #         # swap
            #         self.arr[i],self.arr[j]=self.arr[j],self.arr[i]
            #         moved+=1
            # if swap == False:
            #     break
                
        return moved


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    obj = MinSwap(n,arr)

    res = obj.minimumSwaps()
    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
