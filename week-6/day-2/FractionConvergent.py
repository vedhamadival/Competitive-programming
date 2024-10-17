# Use print() to print to the console
import math
num , den = map(int,input().split())
hcf=math.gcd(num,den)
num=num//hcf
den=den//hcf
print(num ,den ,end=" ")
