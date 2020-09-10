from math import  pow
def dandau(lisst):
    for i in range(0,len(list)-1):
        if (list[i] * list[i+1]) > 0:
            return False
        return  True
def daytang(list):
    for i in range(0,len(list)):
        if list[i+1] - list[i] < 0:
            return  False
        return  True

def CSC(list):
    for i in range (1,len(list)-1):
        if list[i+1] + list[i-1] != 2*list[i] :
            return False
        return  True
def CSN(list):
    if list[0] == 0:
        return False
    for i in range(0,len(list)-2):
        if list[i]*list[i+2] != pow(list[i+1],2):
            return False
    return True
def inputlist(list):
    for i in range(0,len(list)):
        list[i] = float(input('list['+ str(i) + ']='))

n = int(input("Nhap n:"))
list = [0 for i in range (0,n)]
inputlist(list)
#print(daytang(list))
#print(dandau(list))
#print(CSC(list))
#print(CSN(list))