# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# bulb turns on if the it is on and all the prvious are also on.
def solution(A):
    # write your code in Python 3.6
    # for each element push into an array and see if it is consecutive.
    l=[]
    on=0
    for i in A:
        l.append(i)
        # check if l is consecutive?
        n=len(l)
        s=sum(l)
        if s==n*(n+1)/2:
            on+=1
    return on

