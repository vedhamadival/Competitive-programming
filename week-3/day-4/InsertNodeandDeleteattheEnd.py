class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
        return head
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

def delete_at_end(head):
    if head is None:
        return None
    if head.next is None:
        data = head.next
        del head
        return None , data
    current = head
    while current.next.next is not None:
        current = current.next
    data = current.next.data
    del current.next
    current.next = None
    return head, data

def display(head):
    current = head 
    # Traverse the list and print the data of each node
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

# Create an empty head node
head = None
# Read the number of elements in the list
n = int(input())
# Read the elements of the list
arr = list(map(int, input().split()))[:n]
# Insert elements into the list
for i in range(n): 
    head = insert_at_end(head, arr[i])

# Delete the last node of the list and store its data
head, data = delete_at_end(head)
# Display the modified list
display(head)