# Linked_List_Cycle

class Solution(object):
    def hasCycle(self, head):
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow is fast:
                return True
        return False
        