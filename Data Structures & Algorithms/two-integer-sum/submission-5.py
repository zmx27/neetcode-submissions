class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        result = []
        for i in range(len(nums)):
            curr = nums[i]
            other_num = target - curr
            if other_num in num_dict:
                result.append(num_dict[other_num])
                result.append(i)
            else:
                num_dict[curr] = i
        return result

        