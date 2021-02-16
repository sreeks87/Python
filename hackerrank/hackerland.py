#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    liked= 2
    cummulative=2
    shared = 5
    print("Day  Shared  Liked  Cummulative")
    print("1        5     2     2")
    for i in range(2,n+1):
        shared = liked*3
        liked = math.floor(shared/2)
        cummulative = cummulative + liked
        print(i,"    ",shared,"    ",liked,"    ",cummulative)
    return cummulative
        



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    # fptr.write(str(result) + '\n')

    # fptr.close()
















































































































































































































if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    # fptr.write(str(result) + '\n')

    # fptr.close()
