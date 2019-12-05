def quicksort(arr,low,high):
    if low<high:
        pin=partition(arr,low,high)
        quicksort(arr,low,pin-1)
        quicksort(arr,pin+1,high)

def partition(arr,low,high):
    # l=0
    # h=len(arr)-1
    p=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<p:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[i+1],arr[high
    ]=arr[high],arr[i+1]
    return i+1


if  __name__=="__main__":
    arr = [100, 78, 65, 45, 79, 32] 
    n = len(arr) 
    quicksort(arr,0,n-1) 
    for i in range(n): 
        print ("%d" %arr[i]),   