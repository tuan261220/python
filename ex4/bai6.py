def generator(filename):
    list = []
    for line in open(filename,'r',encoding='utf-8'):
        list.append(line.strip())

    return list

def check(list1,list2):
    if len(list1) == len(list2):
        return all(ele in list1 for ele in list2)
    else:
        return False

print(generator('Test1.txt'))
print(generator('Test2.txt'))
if check(generator('Test1.txt'),generator('Test2.txt')) :
    print("Hai file có nội dụng giống nhau")
else:
    print("Hai file có nội dung khác nhau")
