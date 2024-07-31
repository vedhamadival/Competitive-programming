#Leetcode Odd Even Linked List
class Solution(object):
    def oddEvenList(self, head):
        if not head:
            return None

        odd = head
        even = head.next
        evenStart = head.next

        while even and even.next:
            odd.next = even.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = evenStart
        return head
        