def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target and nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[high] <= target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1  

N = int(input())
array = list(map(int, input().split()))[:N]
x = int(input())

result = search(array, x)

if result != -1:
    print(str(result))  # Print the index of the target element
else:
    print(-1)  # Target element not found
