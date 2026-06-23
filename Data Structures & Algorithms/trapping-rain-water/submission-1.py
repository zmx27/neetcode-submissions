class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0] = 0
        rightMax[n-1] = 0

        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i+1])
        
        res = 0
        for i in range(n):
            waterLevel = min(leftMax[i], rightMax[i]) - height[i]
            if waterLevel > 0:
                res += waterLevel
        return res