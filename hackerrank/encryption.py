#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s=s.replace(' ','')
    length=len(s)
    ceil=math.ceil(math.sqrt(length))
    floor=math.floor(math.sqrt(length))
    print(ceil,floor)
    if(ceil*floor>=length):
        parse_array(s,ceil,floor)
    else:
        parse_array(s,ceil,floor+1)

def parse_array(s,c,f):
    str=''
    for i in range(c):
        sum=0
       
        for j in range(f):
            if len(s)>(i+j*c):
                str += s[(i+j*c)]
            else:
                str +=''
        str+=' '
    print(str)
       
       
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    # fptr.write(result + '\n')

    # fptr.close()
