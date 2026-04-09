class Solution(object):
    def generateString(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        n, m = len(str1), len(str2)
        res_len = n + m - 1
        res = [None] * res_len
        
        # Step 1: Fill mandatory characters for all 'T' indices
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if res[i + j] is not None and res[i + j] != str2[j]:
                        return ""  # Conflict found
                    res[i + j] = str2[j]
        
        # Step 2: Fill remaining slots greedily with 'a' or 'b'
        for i in range(res_len):
            if res[i] is None:
                # Try 'a'
                res[i] = 'a'
                # Check if this 'a' causes an invalid 'T' at any relevant position
                # (A 'T' position i means s[i:i+m] MUST equal str2)
                # This is already handled by Step 1.
                
                # Check if this 'a' causes an invalid 'F' (making it a 'T')
                valid_a = True
                for k in range(max(0, i - m + 1), min(i + 1, n)):
                    if str1[k] == 'F':
                        # Check if s[k:k+m] is now equal to str2
                        is_match = True
                        for j in range(m):
                            idx = k + j
                            char = res[idx] if idx != i else 'a'
                            if char is not None and char != str2[j]:
                                is_match = False
                                break
                            if char is None: # Still floating
                                is_match = False
                                break
                        if is_match:
                            valid_a = False
                            break
                
                if not valid_a:
                    res[i] = 'b'
        
        # Step 3: Final validation for 'F' conditions
        for i in range(n):
            substring = "".join(res[i:i+m])
            if str1[i] == 'T' and substring != str2:
                return ""
            if str1[i] == 'F' and substring == str2:
                return ""
                
        return "".join(res)
