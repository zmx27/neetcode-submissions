class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dic:
                return [dic[difference], i]
            dic[nums[i]] = i
        
        