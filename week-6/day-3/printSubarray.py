def print_subarrays(arr, n):
    for i in range(n):
        for j in range(i, n):
            print(*arr[i:j+1])  


n = int(input())
arr = list(map(int, input().split()))
print_subarrays(arr, n)
