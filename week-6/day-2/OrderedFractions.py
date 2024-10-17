num , den=map(int,input().split())
flag=1
for i in range(2,num+1):
  if(num%i==0 and den%i==0):
    n=num//i
    d=den//i
    print(str(n)+'/'+str(d), end=" ") 
    flag=0

if flag==1:
   print(-1)
   



