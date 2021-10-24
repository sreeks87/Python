def WildcardCharacters(str):
    import re
    inpArr= str.split(' ')
    pattern = inpArr[0]
    stringArr = list(inpArr[1])
  
    arr = list(pattern)
    regexp = "/^[A-Za-z]+$/"
    i = 0
    while(i< len(arr)):
        if(arr[i] == '+'):
            if not re.match(stringArr[0],regexp):
                return "false"
            stringArr = stringArr[1:stringArr.length]
        elif arr[i] == '*':
            curr = stringArr[0]
            j = 1
            k = 0
            if len(arr)>i+1 and arr[i+1] == '{':
                k = arr[i+2]
                i = i+4
            else:
                k = 3
                i+=1
            while(j < k):
                stringArr = stringArr[1:stringArr.length]
                if stringArr[0] != curr: 
                    return "false"
                j+=1
            stringArr = stringArr[1:stringArr.length]
            continue
        i+=1
        if stringArr.length != 0:
            return 'false'
        return "true" 

print(WildcardCharacters("+++++* abcdemmmmmm"))