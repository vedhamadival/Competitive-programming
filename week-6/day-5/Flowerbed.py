size = int(input())
n = int(input())
bed = list(map(int,input().split()))

for i in range(size):
    if (bed[i] == 0) and (i == 0 or bed[i-1] == 0) and (i == (size-1) or bed[i+1] == 0):
        bed[i] = 1
        n -= 1
    
    if n == 0:
        print("true")
        break

if n > 0:
    print("false")
        
    


    