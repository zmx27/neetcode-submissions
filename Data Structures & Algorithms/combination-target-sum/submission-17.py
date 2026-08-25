class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        subset = []
        
        def dfs(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return
            elif sum(subset) > target or i == len(candidates):
                return
            else:
                for j in range(i, len(candidates)):
                    if sum(subset) + candidates[j] <= target:
                        subset.append(candidates[j])
                        dfs(j)
                        subset.pop()
        dfs(0)
        return res