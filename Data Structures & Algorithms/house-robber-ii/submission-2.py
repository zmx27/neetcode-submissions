class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        first = nums[0:n-1]
        second = nums[1:n]
        return max(self.helper(first), self.helper(second))

    def helper(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            tmp = rob1
            rob1 = rob2
            rob2 = max(num + tmp, rob2)
        return rob2
        