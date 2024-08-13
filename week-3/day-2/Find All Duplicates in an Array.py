class Solution:
  def findDuplicates(self, nums):
    ans = []

    for num in nums:
      nums[abs(num) - 1] *= -1
      if nums[abs(num) - 1] > 0:
        ans.append(abs(num))

    return ans