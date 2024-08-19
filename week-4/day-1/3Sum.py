# Use print() to print to the console
from typing import List

def threeSum(nums):
    res: List[List[int]] = []
    temp: List[int] = []
    nums.sort() 
    for i in range(len(nums) - 2):
        if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
            lo = i + 1
            hi = len(nums) - 1
            sum = 0 - nums[i]

            while lo < hi:
                if nums[lo] + nums[hi] == sum:
                    temp = [nums[i], nums[lo], nums[hi]]
                    res.append(temp)

                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1

                    lo += 1
                    hi -= 1

                elif nums[lo] + nums[hi] < sum:
                    lo += 1
                else: 
                    hi -= 1
    return res


n = int(input())
arr = list(map(int, input().split()))
ans = threeSum(arr)

if not ans:
    print("No triplet found")
else:
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()
