def max_subarray(a):
    s=0
    currsum=0
    arr=[]
    for i in range(0,len(a)+1):
        for j in range(i,len(a)+1):
            # arr.append(a[i:j])
            currsum=sum(a[i:j])
            if currsum>s:
                s=currsum
                arr=a[i:j]
    return s


# --- 0.0 seconds ---
# [1, 2, 3, -2, 5]
#          36 function calls in 0.002 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 maxsumofsubarrays.py:1(<module>)
#         1    0.000    0.000    0.000    0.000 maxsumofsubarrays.py:1(max_subarray)
#         1    0.001    0.001    0.002    0.002 {built-in method builtins.exec}
#         7    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         2    0.001    0.000    0.001    0.000 {built-in method builtins.print}
#        21    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#         2    0.000    0.000    0.000    0.000 {built-in method time.time}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def kadenes(a):
    maxtillhere=a[0]
    maxsofar=0
        
    for i in range(1,len(a)):
        maxtillhere= max(maxtillhere+a[i],a[i])
        maxsofar=max(maxtillhere,maxsofar)

    return maxsofar

import time
array=[i for i in range(1,100000)]
# print(array)

start_time = time.time()            
res=max_subarray(array)
print("--- %s seconds ---" % (time.time() - start_time))

print(res)

start_time = time.time()            
res=kadenes(array)
print("--- %s seconds ---" % (time.time() - start_time))

print(res)

