
#DecodeString
#56[1[a4[bccd]2[c]]]

def IsANumber(Element):
    try:
        int(Element)
        return  True
    except:
        return  False


def GetChilds(String, TimesLenght):
    StartIndex= TimesLenght+1
    EndIndex= len(String)-1
    Contenuto = String[StartIndex:EndIndex]
    Aperte=0
    Chiuse=0
    Childs=[]
    LastNumberIndex=-1
    LastParantesiClosed=-1
    for x in range(StartIndex, EndIndex):
        Element=String[x]
        if (Element=='['):
            Aperte= Aperte+1
        elif (Element==']'):
            Chiuse=Chiuse+1
        if (Aperte>=2 and Chiuse<=0):
            Childs.append(Contenuto)
            return  Childs

    for x in range(StartIndex, EndIndex):
        SingleElement = String[x]
        # Il numero ha piu cifre le prendo entrambe
        if (IsANumber(SingleElement) and LastNumberIndex != -1):
            LastNumberIndex = LastNumberIndex + x
        # se ne ha solo una prendo solo quella
        elif (IsANumber(SingleElement)):
            LastNumberIndex = x

        if (LastNumberIndex != -1 and SingleElement == ']'):
            LastParantesiClosed = x

        if (LastParantesiClosed != -1 and LastNumberIndex != -1):
            Element = String[LastNumberIndex:LastParantesiClosed + 1]
            Childs.append(Element)
            LastNumberIndex = -1
            LastParantesiClosed = -1
        elif (LastParantesiClosed == -1 and LastNumberIndex == -1):
            Childs.append(SingleElement)

    return Childs






def AreThereLetterOnly(String):
    for x in String:
        if x=='[' or x==']':
            return  False
    return  True

def IsABlock(String):
    Parantesi=0
    for x in String:
        if (x=='[' or x==']'):
            Parantesi= Parantesi+1
        if (Parantesi > 2):
            return False
    return  True


def GetTimesInBlock(Block):

    try:
        if (IsANumber(Block[1])):
            return int(Block[0]+Block[1])
        else:
            return int(Block[0])
    except:
        return  1

def Decode(String):

    if AreThereLetterOnly(String):
        return String
    else:
        Times= GetTimesInBlock(String)
        Childs= GetChilds(String, len(str(Times)))
        tot=''
        for x in Childs:
            tot= tot+Decode(x)
        return Times*tot



if __name__== '__main__':
    textCases= int(input())
    for _ in range (0,textCases):
        Input= input()
        print(Decode(Input))


