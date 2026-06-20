class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort() # Once sum exceed target, all nums after will also exceed
        def backtrack(i, s, path):
            # Base case, found valid combo
            if (s == target):
                res.append(path.copy())
                return
            
            if nums[i] > target: 
                return
            
            for j in range(i, len(nums)): # Start from curr index to avoid dupes
                # If adding curr exceeds, stop
                if s + nums[j] > target:
                    break
                # Include nums[j], backtrack, then undo choice
                path.append(nums[j])
                backtrack(j, s+nums[j], path)
                path.pop()

        backtrack(0, 0, [])
        return res
        