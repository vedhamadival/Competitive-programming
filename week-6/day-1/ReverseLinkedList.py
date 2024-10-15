class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseLinkedList(head):
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev

def printLinkedList(head):
    current = head
    while current is not None:
        print(current.value, end=" ")
        current = current.next
    print()

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))

    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    reversed_head = reverseLinkedList(head)
    printLinkedList(reversed_head)
