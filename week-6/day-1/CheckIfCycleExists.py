# Use print() to print to the console
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def loopHere(head, tail, position):
    if position == 0:
        return

    walk = head
    for i in range(1, position):
        walk = walk.next

    tail.next = walk

def detectLoop(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

n = int(input())

arr = list(map(int, input().split()))[:n]
num = arr[0]
head = tail = Node(num)

for i in range(n-1):
    tail.next = Node(arr[i+1])
    tail = tail.next

pos = int(input())
loopHere(head, tail, pos)

ans = detectLoop(head)
if ans:
    print("True")
else:
    print("False")
