str=input()
foundB=""
foundAC=""
for i in range(len(str)):
  if(i=='b'):
    foundB= True
  if(i=='a' and i+1=='c'):
    foundAC= True

if foundB and foundAC == True:
  print("yes")
else:
  print("no")
