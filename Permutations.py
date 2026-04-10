
class Solution(object):
    def permute(self, nums):
        res = []
        
        def backtrack(current_path):
            # Base Case: If the path length matches nums, we found a permutation
            if len(current_path) == len(nums):
                res.append(list(current_path))
                return
            
            for n in nums:
                # If number is already in path, skip it
                if n in current_path:
                    continue
                
                # Add number and recurse
                current_path.append(n)
                backtrack(current_path)
                
                # Backtrack: remove the last number to try the next one
                current_path.pop()
        
        backtrack([])
        return res
