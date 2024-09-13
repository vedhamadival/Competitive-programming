# Use print() to print to the console
N = input()
count = 0
for i in N:
  if not i.isalpha():
    count +=1
print(count)