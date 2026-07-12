class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # let dp[i] represent min cost to reach step i
        # you can come from either i-1th step or i-2th step
        # the cost is the min of cost[i-1] + dp[i-1] and cost[i-2] + dp[i-2]
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        
        return dp[n]