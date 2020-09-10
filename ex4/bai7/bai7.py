import os
import operator
def countCharacter(filename):
    d = dict()
    text = open(filename,'r',encoding='utf-8')
    for line in text:
        line = line.strip().lower()
        words = line.split(" ")
        for word in words:
            if word in d:
                d[word] +=1
            else:
                d[word] = 1

    return  d

def combinefile():
    with open('test3.txt', 'w', encoding='utf-8') as outfile:
        for names in os.listdir():
            if names == 'bai7.py' :
                continue
            else:
                with open(names, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())

                outfile.write("\n")

    return 'test3.txt'

# d = countCharacter("test1.txt")
d = countCharacter("test.txt")
sorted_dict = sorted(d.items(),key= lambda x : (x[1],x[0]))
# print(sorted_dict)
# print(countCharacter("test1.txt"))
# print(len(sorted_dict))
list = []
# for i in range(6):
#     a = sorted_dict[i][0]
#     list.append(a)
topword = ['s', 'g', 'f', 'd', 'a']
for i in topword:
    if i in d.keys() :
        list.append(d[i])
print(list)
# for i  in list:
#     if str(i[0]) == 'b':
#         list.remove(list[5])
# a.remove(a[len(a)-1])
# list.remove(a)
# print(list - a)