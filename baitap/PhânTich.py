def phantich(n):
    i = 1
    list = []
    for i in range (1,n+1):
        if(n%i==0):
            list.append(i)
    if (len(list) ==  0):
         list.append(n)
    return list

def printN(list,n):
    print(str(n),end="")
    for i in range (0,len(list)):
        for j in range (0,len(list)):
            if list[i]*list[j] == n:
                print("="+ str(list[i]) + "x" + str(list[j]),end="" )
n = int(input('Nhap n :'))
a = phantich(n)
#print(a)
printN(a,n)