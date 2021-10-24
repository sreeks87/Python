def WildcardCharacters(str):
    import re
    strArr= str.split(' ')
    specChar = strArr[0]
    charStr = list(strArr[1])
  
    arr = list(specChar)
    regexp = "/^[A-Za-z]+$/"
    i = 0
    while(i< len(arr)):
        if(arr[i] == '+'):
            if not re.match(charStr[0],letters):
                return "false"
                charStr = charStr[1:charStr.length]
        elif arr[i] == '*':
            curr = charStr[0]
            j = 1
            k = 0
            if len(arr)>i+1 and arr[i+1] == '{':
                k = arr[i+2]
                i = i+4
            else:
                k = 3
                i+=1
            while(j < k):
                charStr = charStr.slice(1,charStr.length)
                if charStr[0] != curr: 
                    return "false"
                j+=1
            charStr = charStr.slice(1,charStr.length)
            continue
        i+=1
        if charStr.length != 0:
            return 'false'
        return "true" 

print(WildcardCharacters("+++++* abcdemmmmmm"))