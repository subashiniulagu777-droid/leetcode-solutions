# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 1. Create a dummy node to handle edge cases (like removing the head)
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # 2. Advance the 'right' pointer n steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1
            
        # 3. Move both pointers together until 'right' reaches the end
        # The gap between left and right is exactly n nodes
        while right:
            left = left.next
            right = right.next
            
        # 4. 'left' is now at the node just BEFORE the one to be deleted
        # Delete the Nth node by skipping it
        left.next = left.next.next
        
        return dummy.next
