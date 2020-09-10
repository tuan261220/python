from _operator import itemgetter
aList = []

print("Nhập vào danh sách theo bộ:tên,tuổi,điểm")

while True:
    s = input("Nhập xâu :").strip()
    if s:
        aList.append(tuple(s.split(",")))
    else:
        break

aList.sort(key=itemgetter(0,1,2),reverse=False)
print(aList)