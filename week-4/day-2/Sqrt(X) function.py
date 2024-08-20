# Use print() to print to the console
def mySqrt(x: int) -> int:
    low, high = 0, x
    ans = 0
    while low <= high:
        if x == 0:
            ans = 0
        mid = low + (high - low) // 2
        sq = mid * mid
        if sq == x:
            return mid
        elif sq > x:
            high = mid - 1
        else:
            low = mid + 1
            ans = mid
    
    return ans


x = int(input())
ans = mySqrt(x)
print(ans)
