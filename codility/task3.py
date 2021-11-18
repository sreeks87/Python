# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# function to rpint fraction, if 1/2==4/8 etc
def solution(X, Y):
    count=0
    # write your code in Python 3.6
    l=[(X[i],Y[i]) for i in range(0,len(X))]
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if (l[i][0]*l[j][1]==l[i][1]*l[j][0]):
                print(l[i],l[j])
                count+=1
    return count

print(solution([1,2,3,4],[2,3,6,8]))