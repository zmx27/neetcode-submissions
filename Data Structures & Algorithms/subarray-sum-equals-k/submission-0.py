class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        prefixSum = {0 : 1} # Starting at index 0, there is a prefix sum of 0 with freq 1 (empty array)
        for num in nums:
            currSum += num
            if (currSum - k) in prefixSum:
                res += prefixSum[currSum-k]
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        return res
