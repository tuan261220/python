import math


def getTop2gram(filename, n):
    '''
    Hàm trả lại danh sách (list) n 2-gram  có số lần nhiều nhất trong file văn bản filename.
    Trong file văn bản filename, mỗi từ phân cách nhau bởi dấu cách, một 2-gram là ghép của 2 từ đi liền nhau trong một dòng,
    ví dụ "a b c d" sẽ có các 2 gram là 'a b', 'b c' và 'c d'
    Danh sách kết quả được sắp xếp giảm dần theo thứ tự từ điển của các 2 gram.
    Nếu 2 2-gram có tần số xuất hiện bằng nhau thì ưu tiên 2-gram có thứ tự từ điển lớn hơn
    (ví dụ 'd a' > 'c a' vì vậy nếu 'd a' và 'c a' có cùng số lần xuất hiện thì lấy 'd a')
    Ví dụ, file văn bản có nội dung như sau:
    "
    a b c a a a b c d f d a d a f g s g h f s s a
    a g h b c e f g m n j s a r t y y u v z x k l a
    "

    danh sách các 2-gram cùng số lần xuất hiện sắp xếp theo số lần xuất hiện tăng dần, 2-gram tăng dần theo thứ tự từ điển như sau:

    [('b c', 3), ('s a', 2), ('g h', 2), ('f g', 2), ('d a', 2), ('a b', 2), ('a a', 2), ('z x', 1),
    ('y y', 1), ('y u', 1), ('x k', 1), ('v z', 1), ('u v', 1), ('t y', 1), ('s s', 1), ('s g', 1),
    ('r t', 1), ('n j', 1), ('m n', 1), ('l a', 1), ('k l', 1), ('j s', 1), ('h f', 1), ('h b', 1),
    ('g s', 1), ('g m', 1), ('f s', 1), ('f d', 1), ('e f', 1), ('d f', 1), ('c e', 1), ('c d', 1),
    ('c a', 1), ('a r', 1), ('a g', 1), ('a f', 1), ('a d', 1)]

    Như vậy với n = 5, kết quả là

   ['s a', 'g h', 'f g', 'd a', 'b c']


    Chú ý, file văn bản có nhiều dòng và không có ký tự unicode
    Nếu n > số 2gram thì kết quả là toàn bộ danh sách các 2gram.
    '''
    d = dict()
    text = open(filename, 'r', encoding='utf-8')
    for line in text:
        line = line.strip().lower()
        words = line.split(" ")
        # print(words[0:len(words)])
        for i in range(len(words) - 1):
            g = ' '.join(words[i:i + 2])
            d.setdefault(g, 0)
            d[g] += 1

    sorted_dict = sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True)
    list = []
    for i in range(n):
        list.append(sorted_dict[i][0])

    c = sorted(list, key=lambda x: x[0], reverse=True)
    return c


def getVector(filename, top2gram):
    '''
        Hàm này trả lại danh sách (list) số nguyên tương ứng với vector biểu diễn văn bản trong file filename.
        phần tử thứ i trong danh sách là số lần top2gram[i] xuất hiện trong văn bản.

        ví dụ văn bản là
        "
        a b c a a a b c d f d a d a f g s g h f s s a
        a g h b c e f g m n j s a r t y y u v z x k l a
        "


        top2gram = ['s a', 'g h', 'f g', 'd a', 'b c']

        kết quả là: [2, 2, 2, 2, 3]

    '''
    d = dict()
    text = open(filename, 'r', encoding='utf-8')
    for line in text:
        line = line.strip().lower()
        words = line.split(" ")
        # print(words[0:len(words)])
        for i in range(len(words) - 1):
            g = ' '.join(words[i:i + 2])
            d.setdefault(g, 0)
            d[g] += 1

    list = []
    for i in top2gram:
        if i in d.keys():
            list.append(d[i])
    return list


def getDistance(u, v):
    '''
        Phương thức tính khoảng cách giữa 2 điểm u, v trên không gian vector

        u = (u1, u2,..., un)
        v = (v1, v2,..., vn)


        ví dụ với u = [1,2,3,4], v = [1,2,1,1], kết quả làm tròn đến 5 chữ số là: 3.60555
    '''
    d = sum([(u[i] - v[i]) ** 2 for i in range(0, len(u))])
    return math.sqrt(d)


def coshTaylor(x, e):
    '''
     Viết chương trình tính sinh(x) theo khai triển Taylor,
     trong đó e là sai số để xác định  thời điểm dừng thuật toán,
     Thuật toán dừng lại tại số hạng Pi nếu |Pi - Pi-1| <= e

     ví dụ x = 5.5, e = 0.00001 kết quả làm tròn đến 5 chữ số là: 122.34801
          nhưng với e = 0.5     kết quả làm tròn đến 5 chữ số là: 92.69794

    '''
    cos = 1
    b = 1
    i = 1
    while (b > e):
        b = (pow(x, 2 * i)) / (math.factorial(2 * i))
        cos += b
        i += 1

    b = (pow(x, 2 * i)) / (math.factorial(2 * i))
    cos += b

    return cos


'''t
    Chú ý, các phương thức sẽ được gọi đến để chấm điểm, 
    do vậy bài nộp của sinh viên cần phải bỏ hết (hoặc comment #) các lệnh in ra màn hình

'''


def testDemo():
    print(getTop2gram('text.txt', 5))
    print(getVector('text.txt', getTop2gram('text.txt', 5)))
    print(round(getDistance([1, 2, 3, 4], [1, 2, 1, 1]), 5))
    print(round(coshTaylor(5.5, 0.5), 5))


'''
Bỏ comment lệnh testDemo() dưới đây để chạy chương trình, và comment lại lệnh đó khi nộp bài
'''
# testDemo()

