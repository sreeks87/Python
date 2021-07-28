import abc


class Solution:
    # a= abc
    # b= adc
    # func(a,b,3,3) c==c, so no change
    # func(a,b,2,2)+0 (no change above)
    # b->d == replace 1 operation
    # func(a,b,1,1)+1+0
    # a->a == no change
    # 0+1+0

    # a=abc
    # b=bcd
    # c!=d ==> so we can Insert/Remove/Replace
    # if we insert, then d will be inserted at the end of s1
    # abcd and bcd; we were at c of a and d of b earlier
    # now we move one step back from the last character in a and b ==>
    # the recursion becomes func(a,b,len(a),len(b)-1)

    # a=abc
    # b=bcd
    # c!=d ==> so we can Insert/Remove/Replace
    # if we remove, then c willbe removed from the end of s1
    # ab and bcd; we were at c of a and d of b earlier
    # now we move one step back from the last character in a and b ==>
    # the recursion becomes func(a,b,len(a)-1,len(b))+1

    # a=abc
    # b=bcd
    # c!=d ==> so we can Insert/Remove/Replace
    # if we replace, then c will be replace with d at the end of s1
    # abd and bcd; we were at c of a and d of b earlier
    # now we move one step back from the last character in a and b ==>
    # the recursion becomes func(a,b,len(a)-1,len(b)-1)+1

    def minDistance(self, word1: str, word2: str) -> int:
        len1=len(word1)
        len2=len(word2)
        return self.edDistanceDP(word1,word2,len1,len2)
    
    def edDistance(self,word1,word2,len1,len2):
        if len1==0:
            return len2
        if len2==0:
            return len1
        if word1[len1-1]==word2[len2-1]:
            return self.edDistance(word1,word2,len1-1,len2-1)

        return 1+ min(self.edDistance(word1,word2,len1,len2-1),
            self.edDistance(word1,word2,len1-1,len2),
            self.edDistance(word1,word2,len1-1,len2-1))
    
    def edDistanceDP(self,word1,word2,len1,len2):
        dp=[[None for i in range(0,len2+1)] for j in range(0,len1+1)]
        # The below is required since a or b can be ==0
        # in that case we may have the nomber of moves == length of other string
        

        for i in range(len1+1):
            for j in range(len2+1):
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                elif word1[i-1]==word2[j-1]:
                    dp[i][j]= dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i][j-1],
                    dp[i-1][j],
                    dp[i-1][j-1])
        return dp[len1][len2]
        

s=Solution()
# a="dinitrophenylhydrazine"
# b="benzalphenylhydrazone"
a="sunday"
b="saturday"
print(s.minDistance(a,b))