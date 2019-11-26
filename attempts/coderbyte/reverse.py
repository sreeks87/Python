def maxMult(lister):
    lister.sort()
    length = len(lister)
    return lister[length-1]*lister[length-2]*lister[length-3]
print maxMult([2,1,-5,4])
