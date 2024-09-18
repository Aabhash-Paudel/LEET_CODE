class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        # Initialize dp table
        dp = [[0] * n for _ in range(n)]
        
        # Fill the dp table
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and length == 2:
                    dp[i][j] = 0
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        
        return dp[0][n-1]