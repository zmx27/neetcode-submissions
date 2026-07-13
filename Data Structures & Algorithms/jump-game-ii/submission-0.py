class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0 
        # l, r represents interval of indices that can be reached with the same number of jumps
        # set l pointer to r+1. 
        # r pointer goes to the farthest index that you can jump to
        
        while r < len(nums) - 1: # only loop until the interval ends at last index
            farthest = 0
            for i in range(l, r+1):
                # i is where you're jumping from, nums[i] is where you can jump to
                farthest = max(farthest, i+nums[i])
            
            l = r+1
            r = farthest
            res += 1
        return res