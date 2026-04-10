class Solution(object):
    def search(self, nums, target):
        i=0
        count=0
        while i<len(nums):
            if target in nums:
                if nums[i]==target:
                    break
                if nums[i]!=target:
                    count+=1
            else:
                count=-1
            i+=1
        return count        