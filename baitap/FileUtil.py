def Move(list):
    list1 = []
    list2 = []
    for i in list:
        if int(i) == 0:
            list1.append(i)
        else:
            list2.append(i)

    return list2 + list1

def zeroMove(filename):
    f = open(filename,'r',encoding='utf-8')
    for line in f:
        numbers = line.strip().split(" ")

    return Move(numbers)

print(zeroMove("abc.txt"))