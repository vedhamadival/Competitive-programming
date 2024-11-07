class Node:
    def __init__(self,data=0):
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None
    curr = head
    
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

head = None
tail = None

N =  int(input())
arr = list(map(int,input().split()))

for i in range(N):
    node = Node(arr[i])
    if head is None:
        head = node
        tail =  node
    else:
        tail.next = node
        tail = node

head = reverse_list(head)

curr = head
while curr is not None:
    print(curr.data , end=" ")
    curr = curr.next
print()