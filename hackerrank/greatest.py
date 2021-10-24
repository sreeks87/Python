def LetterCount(str):
    maxWord = "-1"
    maxCount = 0
    arr = str.split()

    for word in arr:
        d = {}
        c = 0
        for w in list(word):
            if w in d:
                d[w] = d[w] + 1
            else: 
                d[w] = 1
        for k in d:
            if d[k] > 1:
                c = c + d[k]
        if c > maxCount:
            maxWord = word
            maxCount = c

    return maxWord


print(LetterCount("hello apple pie"))