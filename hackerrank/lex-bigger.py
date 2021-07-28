#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#
def anotherpermutation(a,ret,l):
    if len(a)==0:
        l.append(ret)
    for i in range(0,len(a)):
        anotherpermutation(a[0:i]+a[i+1:],ret+a[i],l)
    return l
def biggerIsGreater(w):
    # Write your code here
    m=''    
    l=[]
    anotherpermutation(w,m,l)
    for i in sorted(l):
        if i>w:
            return i
    return "no answer"

        
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
