?- likes(ravi,peanut).
true .
?- likes(ravi,X).
X = apple ;
X = chicken ;
X = peanut .
?- likes(ravi,icecream).
false.

class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # 1. Cyclic Sort: Put each number in its "rightful" place
        # The number x should be at index x - 1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its target index
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # 2. Find the first index where the number is "wrong"
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # 3. If all numbers 1 to n are present, the missing one is n + 1
        return n + 1
