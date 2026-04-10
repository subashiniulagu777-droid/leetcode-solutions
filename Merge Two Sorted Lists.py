# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 1. Create a dummy node to act as the starting point
        dummy = ListNode()
        current = dummy
        
        # 2. While both lists have nodes, attach the smaller value
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        # 3. If one list is longer, attach the remainder
        # In Python, list1 or list2 returns the non-empty one
        current.next = list1 if list1 else list2
        
        return dummy.next
