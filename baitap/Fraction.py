def UCLN(a,b):
    if(b==0):
        return a;
    if a > b :
        return  UCLN(b,b%a)
    return UCLN(a,a%b)
def BSCNN(a,b):
    return int((a*b)/UCLN(a,b))

def toigian(a,b):
    return a/UCLN(a,b),b/UCLN(a,b)

a  = int(input('nhap a:'))
b = int(input('nhap b:'))
print(UCLN(a,b))
#print(toigian(a,b))
#print(BSCNN(a,b))
