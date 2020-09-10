n = int(input('nhap so n = '))
a = 1
if(n%2==0):
    for i in range(2,n+2,2):
        a = a*i
else :
    for i in range(1,n+2,2):
        a = a*i
print(str(n) + '!! = ' + str(a))