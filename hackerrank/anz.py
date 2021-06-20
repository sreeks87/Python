#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'worstLosingStreak' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY nums as parameter.
#

def worstLosingStreak(nums):
    # Write your code here
    max_loss=0
    if(nums == sorted(nums)):
        # print("Sorted array True, price increased return 0")
        return max_loss
    else:
        for i in range(len(nums)):
            # print("I "+str(nums[i]))
            for j in range(i+1,len(nums)):
                # print("J "+str(nums[j]))
                if(nums[i]>nums[j]):
                    # print("i>j")
                    loss=nums[i]-nums[j]
                    # print("loss "+str(loss))
                    if(loss>max_loss):
                        # print("loss>max_loss "+str(loss)+"-"+str(max_loss))
                        max_loss=loss
                        # print("max_loss "+str(max_loss))
        # print("Max loss "+str(max_loss))
        return max_loss
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    result = worstLosingStreak(nums)

    # fptr.write(str(result) + '\n')

    # fptr.close()
