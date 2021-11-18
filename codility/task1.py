# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# write a function to find the max value in the array, max value if only both the negative and positive is present in the array
import sys
def solution(A):
    # write your code in Python 3.6
    d={}
    for i in A:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    maxval=0
    for i in A:
        if i in d and -1*i in d:
            if abs(i)>maxval:   
                maxval=abs(i)
    print(maxval)

    
solution([1,2,3,-4])
