def average(a):
    b = [float(i) for i in a]
    sum = 0
    for i in b :
        sum += i
    return (float)(sum/(len(b)))

def phuongsai(a):
    b = [float(i) for i in a]
    ps = 0
    for i in b:
        ps += (i-average(a))*(i-average(a))

    return (float)(ps/len(b))

a = []
while True:
    s = input("Số = ")
    if s:
        a.append(s)
    else:
        break


print(average(a))
print(phuongsai(a))