s = input("Nhập xâu:")
list = s.split(",")
b = [i for i in list if int(i,2) %5==0]
print(b)
