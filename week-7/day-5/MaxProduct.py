# Use print() to print to the console
def maxProd(nums):
    if len(nums) < 3:
      return 0
    nums.sort()
    return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])

N=int(input())
arr=list(map(int, input().split()))[:N]
print(maxProd(arr))