#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
class TwoD:
    def __init__(self,n,arr):
        self.l=n
        self.arr=arr
    
    def hourglassSum(self):
        w=0
        s=0
        s_lst=[]
        while w<=3:
            v=0
            while v<=3:
                for i in range(3):
                    for j in range(3):
                        
                        if (i==1 and j==0) or (i==1 and j==2):
                            # print('X',end=' ')
                            pass
                        else:
                            # print(self.arr[i+w][v+j],end=' ')
                            s+=self.arr[i+w][v+j]
                    # print('\n')
                v+=1
                s_lst.append(s)
                s=0
                # print("-----")
            w+=1
        return max(s_lst)        


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    arr=[[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
    twod=TwoD(6,arr)
    result = twod.hourglassSum()

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
