'''Một mật khẩu của một tài khoản trên trang web môn học được coi là hợp lệ nếu có
đủ các yếu tố sau:
1. Độ dài từ 8 đến 100 ký tự
2. Có chữ cái in hoa
3. Có chữ cái thường
4. Có số
5. Có ký tự đặc biệt là một trong các ký tự sau: ~!@#$%^&*
Viết chương trình nhập vào một mật khẩu, kiểm tra xem mật khẩu đó có hợp lệ theo
quy tắc ở trên hay không'''
def checklength(str):
    if(len(str) < 8 or len(str) > 100):
        return False
    return True

def checkupper(str):
    num = 0
    for i in str:
        if(i.istitle()):
            num+=1
    return num > 0

def checklower(str):
    num = 0
    for i in str:
        if(i.islower()):
            num+=1
    return num > 0

def checknumber(str):
    num = 0
    for i in str:
        if(i.isalnum()):
            num+=1
    return  num>0

def checkspecialChar(str):
    for i in str:
        if i in ['~','!','@','#','$','%','%','^','&','*']:
            return True
    return False

def check(str):
    if(checkspecialChar(str) and checklength(str) and checkupper(str) and checknumber(str) and checklower(str)):
        return True
    return False
str = input('Nhap xau:')
#print(checkupper(str))
#print('I'.istitle())
print(check(str))