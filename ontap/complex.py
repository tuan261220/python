class ComplexNumber:
    '''
     Lớp thực hiện tạo đối tượng số phức cùng với các phép toán cơ bản,
     số phức (a + bi) có phần thực và phần ảo là số thực
     Các phép toán gồm phép cộng, phép trừ, phép nhân, phép chia.

    '''

    def __init__(self, real, image):
        self.real =real
        self.image = image

    def addComplex(self, frac):
        '''
            Hàm trả lại kết quả là phép cộng của phân số hiện tại với phân số frac
            ví dụ (2+3i)+(4+5i) thì kết quả là (6 + 8i)
        '''

        return ComplexNumber(self.real+frac.real,self.image+frac.image)

    def subComplex(self, frac):
        '''
            Hàm trả lại kết quả là phép trừ của phân số hiện tại với phân số frac
            ví dụ (2+3i)-(4+5i) thì kết quả là (-2 + -2i)
        '''

        self.real = self.real - frac.real
        self.image = self.image - frac.image
        return ComplexNumber(self.real,self.image)

    def multiComplex(self, frac):
        '''
            Hàm trả lại kết quả là phép nhân của phân số hiện tại với phân số frac
            ví dụ (2+3i)*(4+5i) thì kết quả là (-7 + 22i)
        '''
        self.real = self.real*frac.real - self.image*frac.image
        self.image = self.real*frac.image+self.image*frac.real
        return ComplexNumber(self.real, self.image)

    def divComplex(self, frac):
        '''
            Hàm trả lại kết quả là phép chia của phân số hiện tại với phân số frac
            ví dụ (2+3i):(4+5i) thì kết quả là (0.561 + 0.049i)
        '''
        z2 = ComplexNumber(frac.real,-frac.image)
        z = (frac.real**2) + (frac.image**2)
        a = z2.multiComplex(self)
        return ComplexNumber(a.real/z,a.image/z)


    def toString(self):
        '''
            Hàm trả lại chuỗi biểu diễn số phức bởi phần thực và phần ảo làm tròn đến 3 chữ số
            ví dụ phần thực = 5, phần ảo = 3 kết quả là chuỗi '5 + 3i'
            Hàm này được viết sẵn, sinh viên không chỉnh sửa
        '''
        return str(round(self.real, 3)) + ' + ' + str(round(self.image, 3)) + 'i'


'''
    Chú ý, các phương thức sẽ được gọi đến để chấm điểm, 
    do vậy bài nộp của sinh viên cần phải bỏ hết (hoặc comment #) các lệnh in ra màn hình

'''


def testDemo():
    a = ComplexNumber(4, 5)
    b = ComplexNumber(6, 7)
    # print(a.addComplex(b).toString())
    # print(a.subComplex(b).toString())
    print(a.multiComplex(b).toString())
    # print(a.divComplex(b).toString())

testDemo()