from math import sqrt
def solver(a,b,c):
    if(a == 0):
        if(b==0):
            if(c==0):
                print('VSN')
            else:
                print('VN')
        else :
            print(-b/c)
    else :
        delta = b*b - 4*a*c
        if(delta < 0):
            print('VN')
        elif(delta == 0):
            x = (-b - sqrt(delta))/(2*a)
            print(x)
        else :
            x1 = (-b - sqrt(delta))/(2*a)
            x2 = (-b + sqrt(delta))/(2*a)
            print (x1,x2)

a = int(input('nhap so a = '))
b = int(input('nhap so b = '))
c = int(input('nhap so c = '))
solver(a,b,c)