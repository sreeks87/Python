from random import randrange
import time
dict_list = {"listRow1":['1','2','3']
    ,"listRow2": ['4','5','6']
    ,"listRow3": ['7','8','9']
    ,"listRow4": ['1','4','7']
    ,"listRow5": ['2','5','8']
    ,"listRow6": ['3','6','9']
    ,"listRow7": ['1','5','7']
    ,"listRow8": ['3','5','7']
             }
    
def playerInp():
    char1 = raw_input("Enter your character from [O - X - I] :")
    if char1 not in list1:
        print("Thats not right!!! Try again")
        playerInp()
    else:
        return char1
def validInp(inp,char):
    if (int(inp) - 9 >0) or (int(inp) == 0):
        print "Invalid input.Choose valid entry"
        play(char)
    else:
        return True
def replace(char,inp,booln):
    for key_list in dict_list:
        for number in dict_list[key_list]:
            if inp == number:
                index = dict_list[key_list].index(number)
                dict_list[key_list][index] = char
                """dict_list[key_list].remove(inp)"""
    printT(dict_list)
    if game_over(dict_list,char)== True:
        print "You have won!!!"
    else:
        print booln
        if booln == True:
            play_raavan(dict_list,char)
        else:
            play(char)
def game_over(dict_list,char):
    for key_list in dict_list:
        if ((dict_list[key_list][0]==dict_list[key_list][1]==dict_list[key_list][2]=='+') or (dict_list[key_list][1]==dict_list[key_list][2]==dict_list[key_list][0]=='+') or (dict_list[key_list][0]==dict_list[key_list][2] ==dict_list[key_list][1]=='+')):
            return True
        if ((dict_list[key_list][0]==dict_list[key_list][1]==dict_list[key_list][2]==char) or (dict_list[key_list][1]==dict_list[key_list][2]==dict_list[key_list][0]==char) or (dict_list[key_list][0]==dict_list[key_list][2] ==dict_list[key_list][1]==char)):
            return True        
    
def printT(dict_list):
    print" %s    |  %s    | %s  " %(dict_list["listRow1"][0],dict_list["listRow1"][1],dict_list["listRow1"][2])
    print"      |       |     "
    print"-------------------  "
    print"  %s   |   %s   |  %s " %(dict_list["listRow2"][0],dict_list["listRow2"][1],dict_list["listRow2"][2])
    print"      |       |     "
    print"-------------------  "
    print"   %s  |  %s    | %s  " %(dict_list["listRow3"][0],dict_list["listRow3"][1],dict_list["listRow3"][2])
    print"      |       |     "
    print
def play(char):
    inp =raw_input ("Enter your choice [1-9]:")
    if validInp(inp,char) == True:
        replace(char,inp,True)
def play_raavan(dict_list,char):
    time.sleep(5)
    randnum = str(findRand())
    print "rand num %s %s" %(randnum, type(randnum))
    for list in dict_list:
        if randnum in list:
            index1 = dict_list[list].index(randnum)
            print "Index %s" %index1
            replace('+',randnum,False)
            break
        else:
            randnum = str(findRand())
            print "Else %s" %randnum
            
    printT(dict_list)
    play(char)
def findRand():
    randnum = str(randrange(1,9))
    for list in dict_list:
        if randnum in list:
            return randrange(1,9)
            break
        else:
            return findRand()
            break
print "Tic Tac Toe"
list1 = ['O','X','I']
name1 = raw_input("Enter yout screen name :")
name2 = "Raavan"
print "Welcome %s Mind you, you gonna play against RAAVAN" %name1
playerChar = playerInp()
print "My character for action would be +"
print "--------------------------------------------------"
print "                     How to Play                  "
print "Enter the number from the tic tac toe matrix that "
print "you would like to replace with your character     "
print "--------------------------------------------------"
print
printT(dict_list)
"""print"  1   |  2   | 3   "
print"      |      |     "
print"-------------------"
print"  4   |   5  |  6  "
print"      |      |     "
print"-------------------"
print"   7  |  8   | 9   "
print"      |      |     "
print"""
play(playerChar)
