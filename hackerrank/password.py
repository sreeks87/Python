def checker(p):
    import string  
    SpecialSym =list(string.punctuation)
    val = 0
      
    if not "password" in p:
        val +=1

    if len(p) > 7 and len(p)<31:
        val +=1
                   
    if  any(char.isdigit() for char in p):
        val +=1
          
    if  any(char.isupper() for char in p):
        val +=1
          
    if any(char in SpecialSym for char in p):
        val +=1

    if val==5:
        return True
    else:
        return False
  
# Main method

print(checker("password#123!!!#"))
