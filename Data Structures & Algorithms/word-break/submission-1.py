class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                wordLen = len(word)
                # Enough word length and word matches
                if (i + wordLen) <= len(s) and s[i:i+wordLen] == word:
                    dp[i] = dp[i+wordLen]
                if dp[i]: # If found a matching word, continue on to next index
                    break
        
        return dp[0]
                    