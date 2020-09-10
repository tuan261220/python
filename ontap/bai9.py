import  math
def Act(move):
    start = [0,0]
    for i in move:
        if(i[0].lower() == 'up'):
            start[1] += int(i[1])
        elif(i[0].lower() == 'down'):
            start[1] -= int(i[1])
        elif(i[0].lower() == 'left'):
            start[0] -= int(i[1])
        else:
            start[0] += int(i[1])

    return (math.sqrt(math.pow(start[0],2) + math.pow(start[1],2)))

move = []
while True:
    s = input("Nhập hướng di chuyển:").strip()
    if s :
        move.append(tuple(s.split(" ")))
    else:
        break


print(Act(move))

