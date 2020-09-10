def inputMatrix():
    m = []
    x = 0
    while (1):
        n = input()
        if not n:
            break
        part = n.split('\t')
        m += [part]
        x += 1
    mm = [[0 for j in range(0, len(m[i]))] for i in range (0, len(m))]
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            mm[i][j] = (int)(m[i][j])
    return mm

a = inputMatrix()
print(a)