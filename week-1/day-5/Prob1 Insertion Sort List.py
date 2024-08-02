class Solution:
  def insertionSortList(self, head):
    dummy = ListNode(0)
    prev = dummy 

    while head:
      next = head.next 
      if prev.val >= head.val:
        prev = dummy 
      while prev.next and prev.next.val < head.val:
        prev = prev.next
      head.next = prev.next
      prev.next = head
      head = next

    return dummy.next