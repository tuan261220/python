def readfile(filename):
    list = []
    for line in open(filename,'r',encoding= 'utf-8'):
        list.append(line.strip()[::-1])
    return list

def reversefile(filename):
    a = readfile(filename)
    f = open('reverse.txt','w',encoding='utf-8')
    for i in a[::-1]:
        f.write(str(i) + '\n')
    f.close()
    return f

reversefile('input.txt')