# a = 'a b c a a a b c d f d a d a f g s g h f s s a a g h b c e f g m n j s a r t y y u v z x k l a'
# # b = []
# # i = 0
# # while i < (len(a) - 2):
# #     b.append(a[i: i + 3])
# #     i += 2
# # print(b)
# d = dict()
# i = 0
# while i < len(a) - 2:
#     if a[i: i+3] in d :
#         d[a[i: i+3]] += 1
#     else:
#         d[a[i: i+3]] = 1
#     i += 2
# equal = sorted(d.items(), key = lambda x:(x[1], x[0]), reverse = True)
# print(equal)

count = dict()
f = open("text.txt", "rt", encoding="utf-8")
for line in f:
    word = line.split(" ")
    for i in range(len(word) - 1):
        tmp = " ".join(word[i: i+2])
        count.setdefault(0, tmp)
        count[tmp] += 1

countSorted = sorted(count.items(), key = lambda x:(x[1], x[0]), reverse = True)
list = []
for i in range(5):
    list.append(countSorted[i][0])
aList = sorted()