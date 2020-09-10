import  numpy as np
a = np.array([(1, 2, 3), (4, 5, 6)])
print(a)
b = np.array([(0, 5, 25), (4, 9, 9)])
print(b)
d = np.array([(0,3,3) , (1,4,4) , (3,4,5)])
c = np.add(a,b)
c = np.dot(a,d)
print(c)