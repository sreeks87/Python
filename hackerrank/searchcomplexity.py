# /* 
#  * V is sorted 
#  * V.size() = N
#  * The function is initially called as searchNumOccurrence(V, k, 0, N-1)
#  */
# int searchNumOccurrence(vector<int> &V, int k, int start, int end) {
#     if (start > end) return 0;
#     int mid = (start + end) / 2;
#     if (V[mid] < k) return searchNumOccurrence(V, k, mid + 1, end);
#     if (V[mid] > k) return searchNumOccurrence(V, k, start, mid - 1);
#     return searchNumOccurrence(V, k, start, mid - 1) + 1 + searchNumOccurrence(V, k, mid + 1, end);
# }

def searchNumOccurrence(l,k,start,end,c):
    c+=1
    print("Call{c}".format(c=c))
    if start > end: return 0
    mid = (start+end)//2
    # print(mid)
    if l[mid]<k:return searchNumOccurrence(l,k,mid+1,end,c)
    if l[mid]>k:return searchNumOccurrence(l,k,start,mid-1,c)
    return searchNumOccurrence(l,k,start,mid-1,c) + 1+ searchNumOccurrence(l,k,mid+1,end,c)
l =[i for i in range(20)]
print(l)
print(searchNumOccurrence(l,9,0,len(l),0))
