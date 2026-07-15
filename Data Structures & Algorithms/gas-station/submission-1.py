class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas less than total cost, then we can't make a loop
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)):
            if total < 0:
                total = 0
                res = i
            total += (gas[i] - cost[i])
        
        return res

