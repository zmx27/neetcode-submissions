class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        subset = []
        
        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            elif total > target or i == len(candidates):
                return
            else:
                for j in range(i, len(candidates)):
                    if total + candidates[j] <= target:
                        subset.append(candidates[j])
                        dfs(j, total + candidates[j])
                        subset.pop()
        dfs(0, 0)
        return res