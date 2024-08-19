def diffpossible(A,B):
  N=len(A)
  left , right = 0,1

  while left<N and right<N:
    if left!=right and A[right]-A[left]==B:
      return 1
    elif A[right]-A[left]<B:
      right+=1
    else:
      left+=1
  return 0 

N=int(input())
A= list(map(int , input().split()))[:N]
B= int(input())
result=diffpossible(A,B)
print(result)
