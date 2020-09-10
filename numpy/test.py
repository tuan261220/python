import numpy as np
# bai1 : tạo một mảng chiều các số từ 0 đến 30
# a= np.arange(31)
# print(a)

# bai2 : tạo mảng 2 chiều kích thước 3x3 với toàn giá trị True
# trueArray = np.full((3,3),True,dtype=bool)
# print(trueArray)
# b = np.ones((3,3),dtype=bool)
# print(b)

# bài 3: In ra các giá trị chẵn và các giá trị lẻ trong mảng các số nguyên từ 2 đến 20

# a = np.arange(2,21)
#
# print("Các số chẵn trong mảng:",a[a%2==0])
# print("Các số lẻ trong mảng:",a[a%2==1])

# bài 4:Thay thế các giá trị chẵn trong mảng 1 đến 20 bằng -1

# a = np.arange(21)
# print("Mảng trước khi thay đổi",a)
#
# a[a%2==0] = -1
# print("Mảng sau khi thay đổi",a)

# bài 5 :Thay thế các giá trị lẻ trong mảng 2 đến 30 bằng -1 nhưng ko thay đổi mảng ban đầu

# arr = np.arange(2,31)
# # out = np.where(arr % 2 == 1,-1,arr)
# # out  = np.copy(arr)
# # out[out % 2 == 1] = -1
# print(out)
# print(arr)

# bài 6 :Chuyển một mảng 1 chiều kích thước chẵn thành mảng 2 chiều có 2 hàng
#
# arr = np.arange(10)
# if arr.size %2 == 0:
#   print(arr.reshape(2,-1))
#   print(arr)

# bài 7 : Xếp chồng các mảng lên nhau.
# Cho mảng a kích thước 5x2 với các phần tử từ 1 đến 10,
# mảng b cùng kích thước với mảng a và gồm toàn số 1.
# Hãy xếp chồng hàng của mảng a lên trên mảng b.

# a = np.arange(1,11).reshape(5,2)
# b = np.ones((5,2))
# print(np.concatenate([a,b],axis=0))

# bài 8:Đầu vào giống bài 7, nhưng yêu cầu xếp mảng a sang bên trái mảng b

# a = np.arange(1,11).reshape(5,2)
# b = np.ones((5,2))
# print(np.concatenate([a,b],axis=1))


# bài 9 : . Cho mảng a = [1,2,3]
# tạo ra mảng b = [1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# chỉ dùng các hàm của numpy mà không cần khai báo cứng,

# a = [1,2,3]
# c = np.repeat(a,3)
# d = np.tile(a,3)
# print(np.concatenate([c,d],axis=0))


# Bài 10:Lấy ra các giá trị giống nhau trong 2 mảng a,b
# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# print(np.intersect1d(a,b))

# bài 11:Cho 2 mảng a, b. Xóa các phần tử trong mảng a mà cũng có trong mảng b
# a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
#
# print(np.setdiff1d(a,b))

# bài 12:Cho 2 mảng a, b. Lấy ra các vị trí mà tại đó 2 phần tử trong 2 mảng bằng nhau.
# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# print(np.where(a==b))

# bài 13:Lấy các giá trị trong mảng theo điểu kiện
# Cho mảng a,lấy ra các giá trị x trong a thoả mãn 5<=x<=10

# a = np.array([2, 6, 1, 9, 10, 3, 27])
#
# print(a[(a >= 5)&(a<=10)])

# bài 14:Cho 2 mảng a, b có cùng kích thước.
# Xét từng phần tử theo chỉ số mảng, lấy ra phần lớn hơn trong 2 mảng.
# a = np.array([5, 7, 9, 8, 6, 4, 5])
# b = np.array([6, 3, 4, 8, 9, 7, 1])
#
# pair_max = np.vectorize(max)
#
# print(pair_max(a,b))

# bài 15:Đổi chỗ 2 cột trong mảng 2 chiều

# arr = np.arange(1,10).reshape(3,3)
# print(arr)
#
# print(arr[:,[1,2,0]])

# bài 16:Dổi chỗ cột 1 với cột 3

# arr = np.arange(1,10).reshape(3,3)
# print(arr)
# print(arr[[2,0,1],:])

# Bài 17:. Đảo ngược mảng 2 chiều.
# Cho mảng 2 chiều arr, thực hiện đảo ngược thứ tự của mảng 2 chiều.
# Đảo ngược thứ tự các cột, đảo ngược thứ tự các hàng

# arr = np.arange(9).reshape(3,3)
# print(arr)
# print('Đảo ngược các phần tử trong mảng\n',arr[::-1,::-1])
# print('Đảo ngược thứ tự các cột \n',arr[:,::-1])
# print('Đảo ngược thứ tự các hàng \n',arr[::-1,:])

# Bài 18:Tạo một mảng ngẫu nhiên với kích thước 5x3
# Định dạng chỉ in ra 3 chữ số phần thập phân
# Chuyển từ định dạng mũ ex sang dạng bình thường.
# Ví dụ 5.0e-02 => 0.05
# Cho mảng 1 chiều gồm 100 phần tử từ 1 đến 100,
# định dạng để in ra tối đa 6 phần tử trong mảng.
# Ngược lại, định dạng để in ra tất cả các phần tử trong mảng
from numpy.lib.type_check import array_precision

# rand_arr = np.random.random((5,3))
# print(rand_arr)
# np.set_printoptions(precision = 3)
# print(rand_arr)
# rand_arr = rand_arr/1e3
# print(rand_arr)
# np.set_printoptions(suppress=True,precision=5)
# print(rand_arr)
# np.set_printoptions(edgeitems=3,infstr='inf',linewidth=75, nanstr='nan', precision=8,suppress=False, threshold=1000, formatter=None)
# print(rand_arr)

# arr = np.arange(1,20)
# np.set_printoptions(threshold=18)
# print(arr)
#
# import sys
# np.set_printoptions(threshold=sys.maxsize)
# print(arr)