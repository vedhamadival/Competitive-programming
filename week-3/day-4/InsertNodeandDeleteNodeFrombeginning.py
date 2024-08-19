class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def delete(self):
        if self.head is None:
            return None
        new_head = self.head.next
        del self.head
        self.head = new_head
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


llist = LinkedList()
n = int(input())
arr=list(map(int, input().split()))[:n]
for i in range(n):
    llist.insert(arr[i])

llist.delete()
llist.display()
