class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        numSet = set(nums)
        maxLen = 0
        currLen = 0
        for num in numSet:
            if num-1 not in numSet:
                temp = num
                currLen = 1
                while temp + 1 in numSet:
                    currLen += 1
                    temp += 1
                maxLen = max(maxLen, currLen)
        return maxLen