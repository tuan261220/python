a = ';'
list = []
for i in range(1099,9091):
    if(i%11==0):
        if(i%3 != 0):
            list.append(str(i))

b = a.join(list)
print(b)