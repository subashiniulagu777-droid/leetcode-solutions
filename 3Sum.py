class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        # Step 1: Sort the array to use the two-pointer technique
        nums.sort()
        
        for i, a in enumerate(nums):
            # Skip the same value to avoid duplicate triplets in the result
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Use two pointers for the rest of the array
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    # Found a triplet!
                    res.append([a, nums[l], nums[r]])
                    
                    # Move pointers and skip duplicates for the 'l' pointer
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
        return res
