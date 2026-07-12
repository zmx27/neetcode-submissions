class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # At each step, min cost to reach top is cost[i] + min cost from step i+1 or i+2

        # Modify cost[i] in place
        # cost[i] represents min cost to reach top at index n from step i
        for i in range(n-3, -1, -1):
            # Start from third last element, go until index 0
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])