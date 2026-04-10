class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(remain, stack, start):
            if remain == 0:
                # Found a valid combination, add a copy to results
                res.append(list(stack))
                return
            if remain < 0:
                # Exceeded the target, stop this branch
                return

            for i in range(start, len(candidates)):
                # Add the number to our current path
                stack.append(candidates[i])
                # Crucial: pass 'i' as the start index (not i + 1) 
                # because we can reuse the same element
                backtrack(remain - candidates[i], stack, i)
                # Backtrack: remove the number to try the next candidate
                stack.pop()

        backtrack(target, [], 0)
        return res
