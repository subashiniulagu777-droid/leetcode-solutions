class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10**9 + 7
        
        # dp[z][o][0] -> stable arrays ending in 0
        # dp[z][o][1] -> stable arrays ending in 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base cases: single blocks of 0s or 1s within the limit
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        for z in range(1, zero + 1):
            for o in range(1, one + 1):
                # Ending with 0:
                # We take the previous sum ending in 1 and add a 0.
                # If z > limit, we subtract arrays that would exceed the limit.
                dp[z][o][0] = (dp[z-1][o][0] + dp[z-1][o][1]) % MOD
                if z > limit:
                    dp[z][o][0] = (dp[z][o][0] - dp[z-limit-1][o][1] + MOD) % MOD
                
                # Ending with 1:
                # We take the previous sum ending in 0 and add a 1.
                dp[z][o][1] = (dp[z][o-1][0] + dp[z][o-1][1]) % MOD
                if o > limit:
                    dp[z][o][1] = (dp[z][o][1] - dp[z][o-limit-1][0] + MOD) % MOD
                    
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD
