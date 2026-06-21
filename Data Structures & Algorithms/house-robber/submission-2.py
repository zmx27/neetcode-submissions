class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            skip = dp[i-1]
            rob = nums[i] + dp[i-2]
            dp[i] = max(skip, rob)
        
        return dp[len(nums)-1]

