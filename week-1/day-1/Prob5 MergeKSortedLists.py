import heapq

class Solution(object):
    def mergeKLists(self, lists):
        heap = []

        for i , node in enumerate(lists):
            if node:
                heapq.heappush(heap , (node.val , i , node))
        
        d = ListNode()
        curr = d

        while heap:
            val , i , node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap , (node.val, i , node))
        
        return d.next


        