import numpy as  np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# iris = np.genfromtxt(url, delimiter=',', dtype='object')
# names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
#
# print('Kích thước dữ liệu = ',iris.shape)
#
# print('3 dòng đầu của dữ liệu\n',iris[:3])
#
# print('Kiểu dữ liệu'3,type(iris[0,0]))
# print(float(iris[0,0]))

iris = np.genfromtxt(url, delimiter=',', dtype=None,encoding='utf-8')
print('Kích thước dữ liệu = ',iris.shape)

print('3 dòng đầu của dữ liệu\n',iris[:3])
print('Kiểu dữ liệu',type(iris[0][0]))

# label = np.array([row[4] for row in iris])
#
# print('5 nhãn đầu tiên: ',label[:5])
# iris_2d = np.array([row.tolist()[:] for row in iris])
# print('4 dòng đầu \n',iris_2d[:4])
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
print('4 dòng đầu \n',iris_2d[:4])
print('Các giá trị thống kê')
for i in range(0,iris_2d.shape[1]):
  print(iris_2d[:,[i]])
