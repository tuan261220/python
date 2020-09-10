import random
def findUniq(a):
    c = sorted([[x,a.count(x)] for x in set(a)])
    for i in c:
        if(i[1] == 1):
            return i[0]

n = int(input())
a = [random.randint(1,20) for i in range(0,n)]
print(findUniq(a))