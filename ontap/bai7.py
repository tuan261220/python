def money(active):
    money = 0
    for i in active:
        if(i[0] == 'D'):
            money += int(i[1])
        else:
            money -= int(i[1])
    return money

list = []
while(True):
    s = input("Hoạt động:")
    if s:
        list.append(s.split())
    else:
        break

print(money(list))
#print(list[0][0])