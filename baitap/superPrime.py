from math import  sqrt
def isPrime(n):
    if (n < 2):
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

n = int(input('nhap so n = '))
#print(isPrime(n))
if isPrime(n) :
    if(n<10):
        print('True')
    else :
        if(isPrime(int(n/10))):
            print('True')
        else:
            print('False')
else:
    print('False')