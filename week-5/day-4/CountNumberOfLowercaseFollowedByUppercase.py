# Use print() to print to the console
Str = input().strip()
count = 0
for i in range(0,len(Str)-1):
  if Str[i].islower() and Str[i+1].isupper():
    count +=1

print(count)
    
