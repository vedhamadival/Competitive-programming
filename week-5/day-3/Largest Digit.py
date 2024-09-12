# Use print() to print to the console
s,d=map(int, input().split())
if s<=9*d and s>0 and d>0 and d<5 and s<=36:   
    ans=''
    for i in range(d):   
        if s>=9:
            ans+=str(9)  
            s=s-9
        else:
            ans+=str(s)
            s=0 
    print(ans)
else:
    print(-1)