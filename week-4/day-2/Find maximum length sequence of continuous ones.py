# Find the index of 0 to replace with 1 to get the maximum sequence
# of continuous 1's using the sliding window technique
def findIndexofZero(A):
 
    left = 0                
    count = 0               
    max_count = 0
 
    max_index = -1 
    prev_zero_index = -1

    for i in range(len(A)):

        if A[i] == 0:
            prev_zero_index = i
            count = count + 1
        if count == 2:
            while A[left]:
                left = left + 1
            left = left + 1
 
            count = 1
        if i - left + 1 > max_count:
            max_count = i - left + 1
            max_index = prev_zero_index
    return max_index
  
 

 
N=int(input())
#Taking the array elements Input
arr=list(map(int, input().split()))[:N]


index = findIndexofZero(arr)
if index != -1:
    print(index)
else:
    print("Invalid input")
