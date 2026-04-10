class Solution(object):
    def searchRange(self, nums, target):
        if target in nums:
            n=nums.index(target)
            n1=nums[::-1].index(target)
            n1+=1
            count=len(nums)-n1
        else:
            n=-1
            count=-1
        a=[n,count]
        return a
        