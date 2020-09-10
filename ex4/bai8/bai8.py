import os
import math
def computing2grams(filename):
    d = dict()
    text = open(filename,'r',encoding='utf-8')
    for line in text:
        line = line.strip().lower()
        words = line.split(" ")
        # print(words[0:len(words)])
        for i in range(len(words)-1):
            g = ' '.join(words[i:i+2])
            d.setdefault(g,0)
            d[g] += 1
    return d

def combinefile():
    with open('test3.txt', 'w', encoding='utf-8') as outfile:
        for names in os.listdir():
            if names == 'bai8.py' :
                continue
            else:
                with open(names, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())

                outfile.write("\n")

    return 'test3.txt'

d = computing2grams('test1.txt')
sorted_dict = sorted(d.items(),key = lambda x: (x[1],x[0]),reverse=True)
list  = []
top2gram = ['s a', 'g h', 'f g', 'd a', 'b c']
# for i in range(5):
#     list.append(sorted_dict[i][0])
#
# c = sorted(list,key=lambda x:x[0],reverse=True)
# print(c)
for key in d.keys():
    print(key,end=" ")
for i in top2gram :
    if i in d.keys() :
        list.append(d[i])

print(list)


def coshTaylor(x, e):
    cos = 1
    b = 1
    i = 1
    while (b > e):
        b = x ** (2 * i) / (math.factorial(2 * i))
        cos += b
        i += 1

    b = x**(2*i)/(math.factorial(2*i))
    cos += b

    return cos
print(coshTaylor(3.4,0.0001))
# f = open("test1.txt",'r',encoding='utf-8')
# print(f.readline())