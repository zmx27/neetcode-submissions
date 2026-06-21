class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1} # Set base case of when i goes to end of the list, meaning it's valid
        
        def dfs(i):
            if i in dp:
                return dp[i] 
            
            if s[i] == "0":
                return 0
            
            res = dfs(i+1) # Take single digit
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                # Check if i+1 is in bounds, then take if two digits are between 10-26
                res += dfs(i+2)
            dp[i] = res
            return res
        
        return dfs(0)
            
