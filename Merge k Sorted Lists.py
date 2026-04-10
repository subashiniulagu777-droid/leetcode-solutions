import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 1. Initialize the Min-Heap
        min_heap = []
        
        # 2. Push the head of each non-empty list into the heap
        # We include 'i' (the index) as a tie-breaker in case two nodes 
        # have the same value (since ListNode is not directly comparable).
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))
        
        # 3. Create a dummy node to build the result list
        dummy = ListNode(0)
        current = dummy
        
        # 4. While there are nodes in the heap
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            
            # Attach the smallest node to our result
            current.next = node
            current = current.next
            
            # If the popped node has a next node, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next
