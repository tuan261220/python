from _operator import itemgetter

def Sort(a,b):
    aList = []
    aList.append(a)
    aList.append(b)
    aList.sort(key=itemgetter(0),reverse=False)
    return aList[0],aList[1]

def findCouple(filename):
    f = open(filename,"r",encoding= "utf-8")
    while(True):
        string = f.read().split()
        if string:
            new = string[::-1]
            for a in string :
                for b in new:
                    if (a[::-1] == b):
                        return Sort(a,b)
        return(None,None)

print(findCouple("filename.txt"))