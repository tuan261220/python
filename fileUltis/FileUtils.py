import  os
import operator
def checkX(filename,x):
    for line in open(filename,'r',encoding='utf-8'):
        if x in line:
            return (filename,line)

def searchInFiles(x,path):
    list = []
    for filename in os.listdir(path):
        list.append(checkX(filename,x))

    res = sorted(list,key = lambda list:list[0])
    return res


path = "C:\\Users\\DELL\\PycharmProjects\\python\\fileUltis"
print(searchInFiles('a',path))
