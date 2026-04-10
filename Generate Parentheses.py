class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        def backtrack(open_count, close_count, current_string):
            # Base Case: If the string length reaches 2*n, we've found a valid combination
            if len(current_string) == 2 * n:
                res.append(current_string)
                return
            
            # Rule 1: We can add an opening bracket if we haven't used all 'n' of them
            if open_count < n:
                backtrack(open_count + 1, close_count, current_string + "(")
                
            # Rule 2: We can add a closing bracket ONLY if there are unmatched open brackets
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_string + ")")
        
        # Start recursion with 0 open and 0 closed brackets
        backtrack(0, 0, "")
        return res
