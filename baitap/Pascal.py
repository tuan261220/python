# value(n,k) = n!/n!*(n-k)!
from  math import  factorial
def factorial(n):
    fac = 1
    for i in range(1,n+1) :
        fac *=i;
    return fac
def create(i,j):
    return (int)( factorial(i) / (factorial(j)*factorial(i-j)) )
def printPS(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(create(i,j),' ',end='')
        print()
n = int(input('nhap n:'))
printPS(n)
#print(factorial(5))
