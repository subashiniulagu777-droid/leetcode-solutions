class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Step 1: Sort the array to enable two-pointer movement
        nums.sort()
        
        # Initialize with the sum of the first three numbers
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            # Optimization: Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                # If we found the exact target, return immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if the new sum is nearer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on comparison with target
                if current_sum < target:
                    l += 1
                else:
                    r -= 1
                    
        return closest_sum
