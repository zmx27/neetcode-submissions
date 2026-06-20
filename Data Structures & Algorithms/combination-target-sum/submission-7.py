class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, s, path):
            if (s == target):
                res.append(path.copy())
                return
            
            for j in range(i, len(nums)):
                if s + nums[j] > target:
                    return
                # Decision 1: Include nums[j]
                path.append(nums[j])
                backtrack(j, s+nums[j], path)
                path.pop()

        backtrack(0, 0, [])
        return res
        