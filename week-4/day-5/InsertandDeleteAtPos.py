# Use print() to print to the console
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert(headRef, val, i):
    newNode = Node(val)
    if i == 0:
        newNode.next = headRef
        headRef = newNode
    else:
        temp = headRef
        for j in range(i - 1):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode
    return headRef

def remove(headRef, i):
    if headRef is None:
        print("List is empty")
        return headRef
    nodeToRemove = headRef
    if i == 0:
        headRef = headRef.next
        del nodeToRemove
    else:
        for j in range(i - 1):
            nodeToRemove = nodeToRemove.next
            if nodeToRemove is None:
                print("Invalid position")
                return headRef
        temp = nodeToRemove.next
        if temp is None:
            print("Invalid position")
            return headRef
        nodeToRemove.next = temp.next
        del temp
    return headRef

def display(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

if __name__ == "__main__":
    n = int(input())
    head = None
    arr=list(map(int, input().split()))[:n]
    for i in range(n):
        head = insert(head, arr[i], i)
    m, x = map(int, input().split())
    head = insert(head, m, x)
    y = int(input())
    head = remove(head, y)
    display(head)