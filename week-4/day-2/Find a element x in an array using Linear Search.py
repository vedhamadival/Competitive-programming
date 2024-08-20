# Use print() to print to the console
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 

if __name__ == '__main__':
    N=int(input())
    arr=list(map(int, input().split()))[:N]
    Target = int(input())
    print(linear_search(arr, Target))