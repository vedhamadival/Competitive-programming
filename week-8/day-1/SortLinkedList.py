class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def createLinkedList(arr):
    head = None
    tail = None
    
    for i in arr:
        node = Node(arr[i])
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = tail.next
    return head

def sortedLinkedList(head):
    if head is None or head.next is None:
        print(-1)
        return
    
    values = []
    current = head
    while current:
        values.append(current.data)
        current = current.next
        
    values.sort()
    current = head
    
    for val in values:
        current.data = val
        current = current.next
    return head

def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data , end ="")
        current = current.data
    print()

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int,input().split()))
    
    head = createLinkedList(head)
    sorted_list = sortedLinkedList(head)
    printLinkedList(sorted_list)
        
        
    