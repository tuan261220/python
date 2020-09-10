def chan(a):
     b = [i for i in a if i %2==0]
     b.sort()
     return b


def le(a):
    b = [i for i in a if i%2==1]
    b.sort(reverse=True)
    return b
def customSort(a):
    c = chan(a) + le(a)
    return  c



a = [2,3,4,5,6]
print(customSort(a))