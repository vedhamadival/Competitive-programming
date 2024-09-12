# Use print() to print to the console
Str = input()
pos , length = map(int, input().split())
string = Str[pos:]


for i in range(length):
  print(string[i] , end="")