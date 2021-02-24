#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    # 1 4 4 4 5 3
    maxCount=0
    for i in range(len(arr)):
        tmpCount=arr.count(arr[i])
        if tmpCount>maxCount:
            maxCount=tmpCount
            val=arr[i]
    return val
    # m=max([arr.count(i) for i in arr])
    # return min([i for i in arr if arr.count(i)==m])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
