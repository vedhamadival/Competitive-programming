class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def findPairs(head , X):
    if head is None or head.next is None:
        print(-1)
        return
    
    elements = []
    current = head
    while current:
        elements.append(current.data)
        current = current.next
    
    seen = set()
    
    for num in elements:
        complement = X - num
        if complement in seen:
            print(min(num,complement) , max(num, complement))
            return
        seen.add(num)
    
    print(-1)

def createLinkedList(arr):
    head = None
    tail = None
    
    for i in arr:
        node = Node(i)
        
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head

if __name__ == "__main__":
    n = int(input())
    X = int(input())
    arr = list(map(int,input().split()))

    head = createLinkedList(arr)
    findPairs(head , X)
    
    
    
    