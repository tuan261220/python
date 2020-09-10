class Employee:
    def __init__(self,id,name,year,salary):
        self.id = id
        self.name = name
        self.year = year
        self.salary =  salary
    def getSalary(self):
        return self.salary

class Manager(Employee):

    def getSalary(self):
        return self.salary*(1.25)

class DataScientist(Employee):
    def __init__(self,id,name,year,salary,job):
        super().__init__(id,name,year,salary)
        self.job = job

    def getSalary(self):
        return (1.2)*self.salary + self.job*100

class Developer(Employee):
    def __init__(self,id,name,year,salary,job):
        super().__init__(id,name,year,salary)
        self.job = job

    def getSalary(self):
        return (1.2)*self.salary+ self.job*1000


# # a = DataScientist(100,'Tuan',2000,10000,2)
# # a = Employee(100,'Tuan',2000,10000)
# a = Developer(100,'Tuan',2000,10000,5)
# print("lương của {} nhân việc {}".format(a.__class__.__name__,a.getSalary()))
f = open("test.txt",'r',encoding='utf-8')
employee = []
a = []
i = 0
for line in f :
    a.append(line.strip())
print(a[0].startswith('E'))
# print(a)
for i in range(0,len(a)):
    if str(a[i]).startswith('E'):
        E = Employee(str(a[i]),str(a[i+1]),int(a[i+2]),float(a[i+3]))
        employee.append(E)
    if str(a[i]).startswith('M'):
        M = Manager(str(a[i]), str(a[i + 1]), int(a[i + 2]), float(a[i + 3]))
        employee.append(M)
    if str(a[i]).startswith('DS'):
        DS = DataScientist(str(a[i]), str(a[i + 1]), int(a[i + 2]), float(a[i + 3]),int(a[i+4]))
        employee.append(DS)
    if str(a[i]).startswith('DV'):
        DV =  Developer(str(a[i]), str(a[i + 1]), int(a[i + 2]), float(a[i + 3]),int(a[i+4]))
        employee.append(DV)
# text = str(a[2][0])
# print(text.startswith('DS'))
print(employee)


