def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return (-1, -1)  

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // cols
        col = mid % cols

        element = matrix[row][col]

        if element == target:
            return True
        elif element < target:
            left = mid + 1
        else:
            right = mid - 1
              
    return False  

#Enter number of rows
n = int(input())
#Enter number of columns
m = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
#Enter target
target = int(input())
    
    # Call searchMatrix function
result = searchMatrix(matrix, target)
    
    # Print result
print(result)

