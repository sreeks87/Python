
dict_list = {"listRow1":[1,2,3]
    ,"listRow2": [4,5,6]
    ,"listRow3": [7,8,9]
    ,"listRow4": [1,4,7]
    ,"listRow5": [2,5,8]
    ,"listRow6": [3,6,9]
    ,"listRow7": [1,5,7]
    ,"listRow8": [3,5,7]
             }
for key in dict_list:
    print "Dict %s" %key
    for number in dict_list[key]:
        print "List %d" %number
        if 5 == number:
            index = dict_list[key].index(number)
            print "Index %s" %index
            dict_list[key][index] = '0'
            print dict_list
            '''[key][index]'''
