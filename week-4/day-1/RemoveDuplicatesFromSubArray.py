# Use print() to print to the console
def removeDuplicates(A):
    n = len(A)
    if n == 0:
        return 0  
    s = 0  
    f = 1  

    while f < n:
        if A[f] != A[s]:
            s += 1  
            A[s] = A[f]  
        f += 1  

    return s + 1 

N = int(input())

arr = list(map(int, input().split()))[:N] 
print(removeDuplicates(arr))