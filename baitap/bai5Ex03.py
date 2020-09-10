import locale
from _operator import itemgetter

locale.setlocale(locale.LC_ALL, 'vi_VN.utf-8')
print(locale.getlocale())
def Split(name):
    tokens = name.strip().split(' ')
    fname = ''
    sname = ''
    point = ''
    print(tokens)
    if len(tokens) == 2:
        fname = tokens[0]
        point = tokens[1]
    else:
        fname = tokens[len(fname)-2]
        point = tokens[len(point)-1]
        for i in range(0,len(tokens)-2):
            sname = sname+ tokens[i]+' '
        sname = sname.strip()
    
    return sname, fname,point

def compare(name):
    sname, fname,point = Split(name)
    
    return locale.strxfrm(point)
    


names = []
print('Nhập vào các chuỗi họ tên, mỗi chuỗi trên 1 dòng, ấn Ctrl + Z để kể thúc việc nhập')
while True:
    
    s = input('Tên = ')
    if s:
        names.append(s)
    else:
        break


names.sort(key = compare)

print(names)
