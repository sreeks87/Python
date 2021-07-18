#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    c=0
    container_capacity=[sum(i) for i in container]
    print(sorted(container_capacity))

    total_balls=[sum(i) for i in zip(*container)]
    print(sorted(total_balls))

    if sorted(total_balls)==sorted(container_capacity):
        return "Possible"
    else:
        return "Impossible"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()
