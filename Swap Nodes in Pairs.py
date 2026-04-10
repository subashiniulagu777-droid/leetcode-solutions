# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 1. Create a dummy node to handle the new head of the list
        dummy = ListNode(0, head)
        prev = dummy
        
        # 2. Iterate while there are at least two nodes left to swap
        while prev.next and prev.next.next:
            # Nodes to be swapped
            first = prev.next
            second = prev.next.next
            
            # 3. Perform the swap by changing pointers
            # Connect prev to the second node
            prev.next = second
            # Point first to whatever was after second
            first.next = second.next
            # Point second back to first
            second.next = first
            
            # 4. Move 'prev' forward by two nodes for the next pair
            prev = first
            
        return dummy.next
