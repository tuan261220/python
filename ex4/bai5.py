while True:
    try:
        x = int(input("Nhâp một số nguyên: "))
        break
    except ValueError:
        print("Bạn cần nhập một số nguyên ")