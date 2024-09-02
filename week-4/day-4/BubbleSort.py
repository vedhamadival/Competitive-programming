# Use print() to print to the console
def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		swapped = False

		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if (swapped == False):
			break

if __name__ == "__main__":
  size=int(input())
  data=list(map(int, input().split()))[:size]

bubbleSort(data)

for i in range(len(data)):
  print("%d" % data[i], end=" ")