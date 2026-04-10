class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        # 1. Sort is mandatory to handle duplicates easily
        candidates.sort()

        def backtrack(remain, stack, start):
            if remain == 0:
                res.append(list(stack))
                return
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                # 2. Skip duplicates: if this number is the same as the 
                # previous one in the current loop, skip it to avoid 
                # duplicate combinations like [1, 7] and [1, 7].
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                stack.append(candidates[i])
                # 3. Move to 'i + 1' because each number can only be used once
                backtrack(remain - candidates[i], stack, i + 1)
                stack.pop()

        backtrack(target, [], 0)
        return res
