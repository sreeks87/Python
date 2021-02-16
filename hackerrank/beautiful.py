#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    c=0
    print(len([n for n in range(i,j+1) if abs((n)-rev(n))%k==0]))
    # for n in range(i,j+1):
    #     if abs((n)-rev(n))%k==0:
    #         c+=1
    # return c

def rev(x):
    newnum =0
    while(x>0):
        rem = x % 10 
        newnum = newnum*10+rem
        x = x//10
        
    return newnum

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    # fptr.write(str(result) + '\n')

    # fptr.close()
