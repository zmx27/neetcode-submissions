class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights)-1

        while l < r:
            left, right = heights[l], heights[r]
            curr = min(left, right) * (r-l)
            maxArea = max(maxArea, curr)
            if left < right:
                l += 1
            else:
                r -= 1
        return maxArea