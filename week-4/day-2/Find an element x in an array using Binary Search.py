def binarySearch(array, x, low, high):
    while low <= high:

        mid = low + (high - low)//2
        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

N=int(input())
array=list(map(int, input().split()))[:N]
x= int(input())

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print(str(result))
else:
    print(-1)
