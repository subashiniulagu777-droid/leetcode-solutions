class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 1. Base case: If input is empty, return an empty list
        if not digits:
            return []

        # 2. Mapping of digits to letters (standard phone keypad)
        digit_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        def backtrack(index, current_combination):
            # 3. If we've processed all digits, add the combination to result
            if index == len(digits):
                res.append("".join(current_combination))
                return

            # 4. Get letters corresponding to the current digit
            letters = digit_to_letters[digits[index]]

            # 5. Explore each letter for this digit
            for char in letters:
                current_combination.append(char)
                backtrack(index + 1, current_combination)
                # Backtrack: Remove the letter before trying the next one
                current_combination.pop()

        backtrack(0, [])
        return res
