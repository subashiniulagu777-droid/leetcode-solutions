class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # 'insert_pos' tracks where the next unique element should go
        insert_pos = 1
        
        # Start from the second element and compare with the previous one
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                # Found a new unique element
                nums[insert_pos] = nums[i]
                insert_pos += 1
                
        # insert_pos is equal to the number of unique elements
        return insert_pos
