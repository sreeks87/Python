#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the morganAndString function below.
def morganAndString(a, b):
    a=a+'z'
    b=b+'z'
    newString= ""
    # r=len(b) if len(b)<len(a) else len(a)
    for _ in range(len(a)+len(b)):
        if a< b:
            newString+=a[0] if len(a)>0 else ''
            a=a[1:]
        else:
            newString+=b[0] if len(b)>0 else ''
            b=b[1:]
    # if(len(b)>len(a)):return newString + a+b[r:]
    # else:
    return newString[:-1]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()


        result = morganAndString(a, b)

        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
