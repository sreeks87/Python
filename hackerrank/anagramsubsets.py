#User function Template for python3
# Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array. Look at the sample case for clarification.
def Anagrams(words,n):
    '''
    words: list of word
    n:      no of words
    return : list of group of anagram {list will be sorted in driver code (not word in grp)}
    '''
    
    #code here
    ret=[]
    vals=set()
    for i in range(0,n):
        vals.add(words[i])
        for j in range(i+1,n):
            wi=''.join(sorted(words[i]))
            wj=''.join(sorted(words[j]))
            if wi==wj:
                vals.add(words[j])
        ret.append(vals)
        vals=set()
        
    return ret
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ans=Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends