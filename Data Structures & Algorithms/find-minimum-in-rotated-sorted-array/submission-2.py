class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]: # The list is already completely sorted
                res = min(res, nums[l])
                break
            
            m = (r+l) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: # m part of left seg, search right
                l = m+1
            else: # m part of right seg, search left
                r = m-1
        return res
        
        