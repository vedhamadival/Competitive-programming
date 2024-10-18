class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to create a linked list from a list of values
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Function to reverse a linked list
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Function to check if the linked list is a palindrome
def is_palindrome(head):
    # Step 1: Use slow and fast pointers to find the middle of the list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    second_half = reverse_list(slow)

    # Step 3: Compare the first half with the reversed second half
    first_half = head
    second_half_copy = second_half  # Keep a copy of the reversed second half for restoration

    while second_half:
        if first_half.val != second_half.val:
            reverse_list(second_half_copy)  # Restore the original list (optional)
            return False  # Not a palindrome
        first_half = first_half.next
        second_half = second_half.next

    # Step 4: Restore the original list (optional)
    reverse_list(second_half_copy)

    return True  # It is a palindrome

# Input handling and function call
n = int(input())  # Input: Size of the linked list
values = list(map(int, input().split()))  # Input: List of values

head = create_linked_list(values)  # Create the linked list
result = is_palindrome(head)  # Check if the list is a palindrome
print(result)  # Output: True or False
