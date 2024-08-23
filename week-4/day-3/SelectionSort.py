# Use print() to print to the console
def selectionSort(array, size):
   
    for step in range(size):
        min_index = step

        for i in range(step + 1, size):
            if array[i] < array[min_index]:
                min_index = i

        (array[step], array[min_index]) = (array[min_index], array[step])

size=int(input())
data=list(map(int, input().split()))[:size]

selectionSort(data, size)
print(*data)