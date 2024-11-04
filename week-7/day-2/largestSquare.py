def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)
    
    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
        stack.append(i)
    
    return max_area

n = int(input("Enter the size of the histogram: "))
heights = [int(input("Enter height of bar {}: ".format(i + 1))) for i in range(n)]

result = largestRectangleArea(heights)
print(result)
