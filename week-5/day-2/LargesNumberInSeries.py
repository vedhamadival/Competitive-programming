# Use print() to print to the console
N , K = input().split()
K = int(K)
maxim = 0

for i in range(0 , len(N)-K+1):
    d = int(N[i:i+K])
    maxim = max(maxim,d)

print(maxim)






