class Solution(object):
    def removeElement(self, nums, val):
        count=0
        i=0
        while i<len(nums):
            if nums[i]==val:
                count+=1
            i+=1
        j=0
        while j<count:
            nums.remove(val)
            j+=1
        return len(nums)    
        