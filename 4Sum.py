class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 3):
            # Skip duplicate for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicate for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Two-pointer approach for the remaining two numbers
                l, r = j + 1, n - 1
                while l < r:
                    current_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if current_sum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        # Skip duplicates for the third number
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif current_sum < target:
                        l += 1
                    else:
                        r -= 1
        return res
