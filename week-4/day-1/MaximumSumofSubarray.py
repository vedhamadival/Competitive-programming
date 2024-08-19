# Use print() to print to the console
def maximumSubarraySum(arr):
    n = len(arr)
    maxSum = -1e8 
    currSum = 0 

    for i in range(0, n):
        currSum = currSum + arr[i] 

        if currSum > maxSum:
            maxSum = currSum 

        if currSum < 0:
            currSum = 0

    return maxSum


N = int(input())

arr = list(map(int, input().split()))[:N]

max_sum = maximumSubarraySum(arr)

if max_sum == -1e8:
    print(0)
else:
    print(max_sum)
