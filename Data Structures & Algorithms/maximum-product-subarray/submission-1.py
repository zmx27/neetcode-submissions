class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0] # Initialize
        curMin, curMax = 1,1 # Curr min and max values up to that specific number in array
        for num in nums:
            tmp = curMax
            curMax = max(num*curMax, curMin*num, num)
            curMin = min(num*curMin, num*tmp, num)
            res = max(res, curMax)
        return res