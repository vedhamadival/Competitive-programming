#Leetcode PalindromeLinkedList

class Solution(object):
    def isPalindrome(self, head):
        # Array Solution
        # nums = []

        # while head:
        #     nums.append(head.val)
        #     head = head.next
        
        # l , r =0 , len(nums) -1
        # while l <= r:
        #     if nums[l] != nums[r]:
        #         return False
        # return True

        # 
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        left , right = head , prev 
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


        
        