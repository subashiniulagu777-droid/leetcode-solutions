class Solution(object):
    def permuteUnique(self, nums):
        res = []
        nums.sort()  # Sorting is key to handling duplicates
        used = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for i in range(len(nums)):
                # Skip if already used in current path
                if used[i]:
                    continue
                
                # Skip duplicate: if current number is same as previous,
                # AND the previous one wasn't used in this branch yet.
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                
                # Backtrack
                used[i] = False
                path.pop()
        
        backtrack([])
        return res
