s = " sssaaaa bbbaa"
a = s.split()
d = []
for line in a:
    s = {}
    for word in line:
        if word in d:
            s[word] = 1
        else:
            s[word] = 1
    print(s)
print(d)

# g= 'sssaa'
# e = {}
# for line in g:
#     for word in line:
#         if word in e:
#             e[word] = 1
#         else:
#             e[word] = 1
# print(e)
#
# print(new)