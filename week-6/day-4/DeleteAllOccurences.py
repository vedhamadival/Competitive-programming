# Define the structure of a singly linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to delete all occurrences of X from the linked list
def delete_all_occurrences(head, X):
    # Handle the case where the head itself contains the value X
    while head is not None and head.val == X:
        head = head.next  # Move the head to the next node

    # Initialize pointers for traversal
    current = head
    previous = None

    # Traverse the list to remove occurrences of X
    while current is not None:
        if current.val == X:
            # If a match is found, skip the current node
            previous.next = current.next
        else:
            # If not a match, move the previous pointer forward
            previous = current

        # Move the current pointer to the next node
        current = current.next

    return head  # Return the modified head

# Function to print the linked list
def print_linked_list(head):
    result = []
    current = head
    while current is not None:
        result.append(str(current.val))
        current = current.next
    print("".join(result))

# Helper function to create a linked list from input
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Input handling
n = int(input())  # Length of the linked list
values = list(map(int, input().strip()))  # List of node values
X = int(input())  # Value to be deleted

# Create the linked list
head = create_linked_list(values)

# Delete all occurrences of X
head = delete_all_occurrences(head, X)

# Print the modified linked list
print_linked_list(head)
