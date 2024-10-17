def setcol(matrix, m, n, j):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def setrow(matrix, m, n, i):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def setZeroes(matrix, m, n):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                setrow(matrix, m, n, i)
                setcol(matrix, m, n, j)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix

n, m = map(int, input().split())
matrix = []

for i in range(n):
    rows = []
    values = input().split()
    for j in values:
        rows.append(int(j))
    matrix.append(rows)

result = setZeroes(matrix, m, n)
for i in range(n):
    for j in range(m):
        print(result[i][j], end=" ")
    print()

