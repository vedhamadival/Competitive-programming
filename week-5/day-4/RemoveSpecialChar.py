# Use print() to print to the console
Str = input()
l1=[]

for i in Str:
  if i.isalpha():
    l1.append(i)

print("".join(l1))