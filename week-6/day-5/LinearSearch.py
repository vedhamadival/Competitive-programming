def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    # write your code here
    return -1 

N=int(input())
#Taking the array elements Input
arr=list(map(int, input().split()))[:N]
Target = int(input())
print(linear_search(arr, Target))
