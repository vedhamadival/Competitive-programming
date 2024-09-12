# Use print() to print to the console
N = int(input())
s1 = 0 #square of summ
s2 = 0 #summ of squares

for i in range(1, N+1):
  s1 += i
for j in range(1, N+1):
  s2 += j**2
print(abs(s1**2 - s2))