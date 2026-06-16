class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n
        pref[0] = 1
        suff[n-1] = 1
        for i in range(1, n): # 1 to n-1
            pref[i] = nums[i-1] * pref[i-1]
        for j in range(n-2, -1, -1): # n-2 to 0
            suff[j] = nums[j+1] * suff[j+1]
        for k in range(n):
            res[k] = suff[k] * pref[k]
        return res
        