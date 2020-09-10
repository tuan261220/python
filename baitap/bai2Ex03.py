'''Viết chương trình sinh ngẫu nhiên danh sách các số nguyên trong khoảng từ 0 đến
N, với N nhập từ bàn phím. Tìm và in ra giá trị lớn nhất, giá trị nhỏ nhất trong danh
sách. In ra phần tử xuất hiện nhiều nhất trong danh sách và số lần xuất hiện của phần
tử đó.'''
import numpy as np
def getMax(a,n):
    count = [0] * 256
    max = -1;
    c = ' '
    for i in a:
        count[i] += 1;

    for i in a:
        if max < count[i]:
            max = count[i]
            c = i

    return c,max
n = int(input("Nhập n:"))
a = np.random.randint(n,size=n)
print(a)
print(max(a))
print(min(a))
print(getMax(a,n))