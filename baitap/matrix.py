def minrow(matrix,i):
    min = matrix[i][0]
    for j in range (0,len(matrix[0])):
        if matrix[i][j] < min :
            min = matrix[i][j]
    return  min
def maxcol(matrix,j):
    max = matrix[0][j]
    for i in range(0,len(matrix)):
        if matrix[i][j] > max:
            max = matrix[i][j]
    return max
def check(matrix,i,j):
    if(matrix[i][j] == minrow(matrix,i)):
        if matrix[i][j] == maxcol(matrix,j):
            return True
    return False
def printCheck(matrix):
    c = []
    for i in range (0,len(matrix)):
        for j in range (0,len(matrix[0])):
            if check(matrix,i,j):
                    c.append(matrix[i][j])

    return c
A = [[-8, 5,5, 7],
 [-7, 6, 9, 0],
 [13, 7, 11, 19]]
#print(minrow(A,2))
#print(maxcol(A,3))
#print(check(A,2,0))
print(printCheck(A))

