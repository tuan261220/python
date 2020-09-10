def solve(matrix):
    n = len(matrix)
    s = 0
    for i in range (0,n):
        s += matrix[i][i]

    s1= 0
    for i in range (n):
        s1 += matrix[i][n-1-i]
    if (s1 != s) :
        return False

    for i in range (n):
        rowSum = 0
        for j in range (n):
            rowSum += matrix[i][j]
        if rowSum != s:
            return  False

    for i in range (n):
        colSum = 0
        for j in range (n):
            colSum+= matrix[j][i]
        if colSum != s:
            return  False
    return True

'''mat = [ [ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ],
        [ 9, 10, 11,12 ],
        [13,14,15,16] ]
if(solve(mat)):
    print("Magic Square")
else:
    print("Not Magic Square")'''
def inputMatrix():
    m = [][]
    for i in range(len(m)):
        for j in range (len(m[0])):
            pt = int(input())
            m[i][j].append(pt)
    return m