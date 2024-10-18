N = int(input())

matrix = []
for i in range(N):
    row = list(map(int,input().split()))
    matrix.append(row)

for i in range(N):
    for j in range(i,N):
        matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
    
for i in range(N):
    matrix[i].reverse()

for row in matrix:
    print(" ".join(map(str,row)))
    