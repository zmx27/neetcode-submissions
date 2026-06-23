class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l]) # Curr could be larger than leftMax
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r]) # Curr could be larger than rightMax
                res += rightMax - height[r]
        return res