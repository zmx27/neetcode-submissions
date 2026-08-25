class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if total + candidates[i] <= target:
                    subset.append(candidates[i])
                    dfs(i+1, candidates[i] + total)
                    subset.pop()
                    while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                        i += 1
                    dfs(i+1, total)
        dfs(0, 0)
        return res