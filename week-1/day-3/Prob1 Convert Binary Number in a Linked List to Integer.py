# Leetcode Convert Binary Number in a Linked List to Integer
class Solution(object):
    def getDecimalValue(self, head):
        n1 = head
        store = ''

        while n1 is not None:
            store += str(n1.val)
            n1 = n1.next
        return int(store , 2)
        