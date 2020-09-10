#Viết chương trình đếm các ký tự trong văn bản sử dụng Cấu trúc dữ liệu Từ điển
s = "pham quang tuan"
def count(s):
    d = {}
    for i in s.lower():
        d[i] = d.get(i,0)+1
    return d

print(count(s))