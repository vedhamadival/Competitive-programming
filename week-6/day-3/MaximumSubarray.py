N = int(input())
array = list(map(int , input().split()))

max_current = array[0]
max_global = array[0]

for i in range(1,N):
    max_current = max(array[i] , (max_current+array[i]))
    
    if max_current > max_global:
        max_global = max_current
    
print(max_global)
