from math import  sqrt
def check(a,b,c):
    if(a+b > c and a+c > b and b+c>a):
        return True
    return  False
a = float(input('nhap canh a = '))
b = float(input('nhap canh b = '))
c = float(input('nhap canh c = '))
if (check(a,b,c)):
    C = a+b+c
    p = (a+ b + c)/2
    a = p*(p-a)*(p-b)*(p-c)
    s = sqrt(a)
    print('S = ',s,'C = ',C)
else :
    print('INVALID')