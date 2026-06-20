class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, s, path):
            if s == target:
                res.append(path.copy())
                return

            if (i >= len(nums) or s > target):
                return
            
            # Decision 1: Include nums[i]
            path.append(nums[i])
            backtrack(i, s+nums[i], path) # Can possibly keep including nums[i]
            path.pop()

            # Decision 2: Don't include, move on to next num
            backtrack(i+1, s, path)

        backtrack(0, 0, [])
        return res
            