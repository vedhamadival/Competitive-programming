# Use print() to print to the console
def searchRange(nums, target):
    left, right = 0, len(nums) - 1
    first_occurrence = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            first_occurrence = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if first_occurrence == -1:
        return [-1, -1]

    left, right = first_occurrence, len(nums) - 1
    last_occurrence = first_occurrence

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            last_occurrence = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return [first_occurrence, last_occurrence]

N=int(input())
array=list(map(int, input().split()))[:N]
x= int(input())


result = searchRange(array, x)
print(result[0], result[1])

