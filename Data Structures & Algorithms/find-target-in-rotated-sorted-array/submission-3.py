class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (r+l) // 2
            if (nums[m] > nums[r]):
                l = m+1
            else:
                r = m
        pivot = l # Binary search to find the min/pivot
        l = 0
        r = len(nums) - 1
        if (nums[pivot] <= target and target <= nums[r]):
            l = pivot
        else:
            r = pivot - 1
        while l <= r: # Decide which half target is in and do another binary search
            m = (r+l) // 2
            if (nums[m] == target):
                return m
            elif (nums[m] < target):
                l = m+1
            else:
                r = m-1
        return -1
            

        