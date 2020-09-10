string = []
while(True):
    s = input("Nhập xâu :")
    if s :
        string.append(s)
    else:
        break

a = {x: x[0::]+x[::-1] for x in string}
print(a)