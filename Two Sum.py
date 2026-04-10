class Solution(object):
    def twoSum(self, nums, target):
        i=0 
        while i<len(nums)-1:
            if (nums[i]+nums[i+1]) == target:
                return [i,i+1]
            
            i+=1    