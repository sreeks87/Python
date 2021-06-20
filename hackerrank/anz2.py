#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countingUniversalSubarrays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingUniversalSubarrays(arr):
    # Write your code here
    sublists=[[]]
    one=two=False
    found2=found4=False
    count=0
    for i in range(len(arr)+1):
        for j in range(i):
            sublists.append(arr[j:i])
    print(sublists)
    for s in sublists:
        if(len(s)>=2):
            # condition 1
            print(s)
            if(2 in s and 4 in s):
                n2=min(k for k,v in enumerate(s) if v==2)
                x2=max(k for k,v in enumerate(s) if v==2)

                n4=min(k for k,v in enumerate(s) if v==4)       
                x4=max(k for k,v in enumerate(s) if v==4)
                print(n2,x2,n4,x4)
            # n4 should not be between n2 and x2
            # n2 should not be between n4 and x4
                if(n4>n2 and n4<x2) or (n2>n4 and n2<x4):
                    print("print one "+ str(s))
                    one=False
                else:
                    print("Condition one satisfied for "+ str(s))
                    one=True
        
            # condition 2
            if(one and (s.count(4)==s.count(2))):
                print("Condition two satisfied for "+str(s))
                two=True
            else:
                two=False
            if(one and two):
                print("one and two for "+str(s))
                count+=1
        print("------")
    print(count)
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = countingUniversalSubarrays(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
