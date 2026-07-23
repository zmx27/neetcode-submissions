class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        l, r = 0, len(height) - 1
        res = 0
        leftMax, rightMax = height[l], height[r]
        # Water depends on the shorter wall between the leftmax and rightmax
        while l < r:
            if leftMax < rightMax:
                # left wall is shorter
                res += max(leftMax - height[l], 0)
                l += 1
                leftMax = max(leftMax, height[l])
            else:
                res += max(rightMax - height[r], 0)
                r -= 1
                rightMax = max(rightMax, height[r])
        return res
