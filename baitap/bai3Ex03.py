'''Nhập vào một xâu, in ra số lượng chữ cái, số lượng chữ số, số lượng các ký tự khác
(không phải chữ cái – không phải số) trong xâu vừa nhập.'''
def count(str):
    num = 0
    alpha = 0
    other = 0
    for i in str:
        if(i.isalpha()):
            alpha+=1
        elif(i.isalnum()):
            num+=1
        else:
            other+=1
    return num,alpha,other

str = input("Nhap xau:")
print(count(str))
print('11'.isalpha())