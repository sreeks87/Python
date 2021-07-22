# Find all possible palindromic partitions of a String

#User function Template for python3

class Solution:
    def allPalindromicPerms(self, S):
        # code here 
        l=0
        ss=''
        for i in range(0,len(S)+1):
            for j in range(i,len(S)+1):
                string=S[i:j]
                if(string != '' and len(string)>1 and self.pal(string)):
                    if len(string)>l:
                        ss=string
        return ss

    def pal(self,s):
        if s=='':
            return True
        elif s[0]==s[-1]:
            return self.pal(s[1:-1])
        else:
            return False
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        allPart = ob.allPalindromicPerms(S)
        
        for i in range(len(allPart)): 
            for j in range(len(allPart[i])): 
                print(allPart[i][j], end = " ") 
            print() 
# } Driver Code Ends


# def palindrome(s):
#     return s == '' or (s[0]==s[-1] and palindrome(s[1:-1]))

# print(palindrome('madamf'))



# print(pal('madam'))
# print(b)