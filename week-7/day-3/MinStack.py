class Minstack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    
    def push(self, val: int):
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
    
    def pop(self):
        if not self.stack:
            return -1
        popval = self.stack.pop()
        if popval == self.minstack[-1]:
            self.minstack.pop()
        return popval
    
    def getMin(self):
        if not self.minstack:
            return -1
        return self.minstack[-1]

# Read the number of operations
N = int(input())
minstack = Minstack()

# Prepare to collect output results
output = []

# Process each operation
for _ in range(N):
    query = list(map(int, input().split()))
    operation = query[0]
    
    if operation == 1:  # Push operation
        value = query[1]
        minstack.push(value)
    elif operation == 2:  # Pop operation
        result = minstack.pop()
        output.append(result)  # Collect result
    elif operation == 3:  # Get minimum operation
        result = minstack.getMin()
        output.append(result)  # Collect result

# Print all collected results in a single line
print("".join(map(str, output)))
