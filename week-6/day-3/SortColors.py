N = int(input())
nums = list(map(int , input().split()))

low , mid , high = 0 , 0 , len(nums)-1

while mid <= high:
    if nums[mid] == 0:
        nums[low] , nums[mid] = nums[mid] , nums[low]
        low+=1
        mid+=1
    elif nums[mid] == 1:
        mid +=1
    else:
        nums[high] , nums[mid] = nums[mid] , nums[high]
        high -=1

print(" ".join(map(str,nums)))
