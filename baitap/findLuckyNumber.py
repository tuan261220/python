import math
def PrimeNumber(n):
    if(n<2):
        return False
    for i in range(2,int(math.sqrt(n))):
        if n %i == 0:
            return  False
    return True

def luckynumber(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    if(sum % 5 ==0 ):
        return True
    return False


f = open("filename.txt","r",encoding= "utf-8")
while(True):
    number = f.read().split()
    for num in number:
        if num.isdigit():
            if PrimeNumber(int(num)):
                if luckynumber(int(num)):
                    print(num)

