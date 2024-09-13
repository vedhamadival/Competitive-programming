# Use print() to print to the console
N = input()
ans = ""

for i in range(len(N)-1):
  if N[i].islower() and N[i+1].isupper():
    ans+=N[i]
    ans+=" "
  else:
    ans+=N[i]

j = ans+N[i+1]

print(j)

    


    