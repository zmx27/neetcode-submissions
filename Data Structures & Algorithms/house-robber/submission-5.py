class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0 # Max up to house i-2
        rob2 = 0 # Max up to house i-1
        
        for num in nums:
            tmp = rob1
            rob1 = rob2
            rob2 = max(num + tmp, rob2)

        
        return rob2