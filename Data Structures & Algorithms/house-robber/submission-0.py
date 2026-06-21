class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = len(nums) * [-1]

        def dfs(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            
            skip = dfs(i+1)
            rob = nums[i] + dfs(i+2)
            dp[i] = max(skip, rob)
            return dp[i]
        
        return dfs(0)
