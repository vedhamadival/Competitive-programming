# Use print() to print to the console
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1    
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


size=int(input())
data=list(map(int, input().split()))[:size]

insertionSort(data)
print(*data)