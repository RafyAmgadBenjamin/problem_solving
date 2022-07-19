
def convCase(s):
    sentc = s.split(';')
    oper = sentc[0]
    typ = sentc[1]
    words = sentc[2]

    newS = ""
    if oper == "S":
        for index, char in enumerate(words): 
            if index == 0 and char >='A' and char <= "Z":
                newS+= char.lower()
            elif char == "(" or char == ")":
                continue
            elif char >='A' and char <= "Z":
                newS += ' '
                newS+= char.lower()
            else:
                newS+= char
    else: # case combine
        # for index, char in enumerate(words):
        index = 0
        while index < len(words):
            if words[index] == " ":
                newS += words[index+1].upper()
                index+=1
            else:
                newS += words[index]
            index+=1

        if typ == "M":
            newS+="()"
        
        elif typ == "C":
            newS= newS[0].upper() + newS[1:]
        else:#V
            pass

    print(newS)
        





if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    convCase(s)

    # fptr.close()
