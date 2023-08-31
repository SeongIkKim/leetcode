class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        dp[i][j]
        i and j is min # of operations required to transfrom from word1[0..i-1] to word2[0..j-1]
        dp[0][0] didn't consider anything yet.
        dp[m][n] considered every converting case from whole word1 to whole word2.
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            dp[i][0] = i # have to delete all letters
        
        for j in range(1, n+1):
            dp[0][j] = j # have to add all letters
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] # pass this index without operation
                else:
                    dp[i][j] = min(
                        dp[i-1][j-1], # replace
                        dp[i][j-1], # insert
                        dp[i-1][j] # delete
                        ) + 1 # takes 1 operation
        return dp[m][n]

        return ans
            
