k = int(input())
s = input()
maxim=0

for i in range(0 , len(s)-k+1):
  substring = s[i:i+k]
  prod = 1
  for j in substring:
    digit = int(j)
    prod *= digit
    
    if digit == 0:
      prod = 0
      break
  maxim = max(maxim , prod)

print(maxim)


  


    




