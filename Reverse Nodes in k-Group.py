# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 1. Create a dummy node to simplify head management
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # 2. Find the kth node from the current group_prev
            kth = self.getKth(group_prev, k)
            if not kth:
                break # Not enough nodes left to reverse
            
            # Store the node after the group to reconnect later
            group_next = kth.next
            
            # 3. Reverse the group (Standard Linked List Reversal)
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # 4. Reconnect the reversed group to the rest of the list
            temp = group_prev.next # The old head of the group is now the tail
            group_prev.next = kth  # group_prev now points to the new head
            group_prev = temp      # Move group_prev to the tail for the next iteration
            
        return dummy.next

    def getKth(self, curr, k):
        # Helper to find the kth node relative to curr
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
