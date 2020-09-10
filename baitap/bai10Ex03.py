import  math
import random
def tinhtu(u,v):
    return sum([u[i]*v[i] for i in range (0,len(u))])


def tinhmau(u):
    x = sum([pow(i,2) for i in u])
    y = round(math.sqrt(x),4)
    return y

def cosin(u,v):
    tu = tinhtu(u,v)
    mau = tinhmau(u) * tinhmau(v)
    a = (tu/mau)
    return  a

def maxC(x):
    max = -1;
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            print(cosin(x[i],x[j]))
            if(cosin(x[i],x[j]) > max):
                max = cosin(x[i],x[j])
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if(max == cosin(x[i],x[j])):
                return x[i],x[j]
def minC(x):
    min = 1;
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if (cosin(x[i], x[j]) < min):
                min = cosin(x[i], x[j])
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if (min == cosin(x[i], x[j])):
                return x[i], x[j]
n = int(input("nhap n:"))
x =[[random.randint(1,2) for i in range(0,15)] for j in range(0,n)]
print(x)
print(maxC(x))
print(minC(x))

'''u = [random.randint(0,3) for i in range(0,15)]
v = [random.randint(0,3) for i in range(0,15)]
print(u)
print(v)
print(cosin(u,v))'''