#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations
#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    p=permutations(w)
    c=0
    for i in p:
        big=''.join(i)
        c+=1
        # if(c==2):
        print('big =='+big)
        if big > w:
            return big
        else:
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
