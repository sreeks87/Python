#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):   
    w= m%n+(s-1)
    if(w==0):
        return n
    if(w>n):
        return w-n
    return w



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        no_of_prisoners = int(nms[0])

        no_sweets = int(nms[1])

        start_at = int(nms[2])

        result = saveThePrisoner(no_of_prisoners, no_sweets, start_at)
        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
