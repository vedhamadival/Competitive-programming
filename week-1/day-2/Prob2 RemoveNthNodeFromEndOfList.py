# Remove Nth node from end of list
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head
        ahead = behind = dummy

        for _ in range(n+1):
            ahead = ahead.next
        
        while ahead:
            ahead = ahead.next
            behind = behind.next
        behind.next = behind.next.next
        return dummy.next