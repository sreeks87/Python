#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
class MinBribe:
    def __init__(self,n,arr):
        self.n=n
        self.arr=arr

    def minimumBribes(self):
        moved=0
        diff=0
        swap=False
        for i in range(1,self.n+1):
            diff=q[i-1]-i
            if diff >0:
                # s=s+diff
                if diff>2:
                    return 'Too chaotic'

        for i in range(self.n):
            # diff=self.arr[i]-i+1
            # if diff>2:
            #     return 'Too chaotic'
            if diff >0:
            # s=s+diff
                if diff>2:
                    return 'Too chaotic'
            if i+1 != self.arr[i]:
                # do bubble
                for j in range(i+1,n):
                    if self.arr[i]>self.arr[j]: 
                        # swap
                        self.arr[i],self.arr[j]=self.arr[j],self.arr[i]
                        moved+=1
                        swap=True
                if swap == False:
                    break
                
        return moved


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        obj=MinBribe(n,q)
        print(obj.minimumBribes())
        # print(obj.minimumBribes(q))



# 1 2 5 3 7 8 6 4

# 1 2 3 4 5 6 7 8
# 1 2 3 5 4 6 7 8 --1
# 1 2 5 3 4 6 7 8 --2
# 1 2 5 3 4 7 6 8 --3
# 1 2 5 3 7 4 6 8 --4
# 1 2 5 3 7 4 8 6 --5
# 1 2 5 3 7 8 4 6 --6
# 1 2 5 3 7 8 6 4 --7

# num bribed  been bribed

# 1   0       0
# 2   0       0
# 3   0       1
# 4   0       4
# 5   2       0
# 6   0       1
# 7   2       0
# 8   2       0


# 1 2 4 5 3 6 7 8
# 0 0 2 -1 2 2 -1 -4 
# 0 0 2 0 2 2 0 0

