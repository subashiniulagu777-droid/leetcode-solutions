class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            a=nums.index(target)
        else:
            i=0
            c=0
            while i<len(nums):
                if target > nums[i]:
                    c+=1
                else:
                    break
                i+=1
            a=c
        return a    

         
        