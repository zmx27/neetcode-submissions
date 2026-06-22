class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        # Find first index i where nums[i] < nums[i+1]
        # This is because segment after i is in decreasing order, which is already the highest possible permutation
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # If found, find next highest element after index i at index j
        if i >= 0:
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap i and j
            nums[i], nums[j] = nums[j], nums[i]
        
        # Deal with segment after index i, which we know is in decreasing order and maximum possible permutation
        l, r = i+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l] # Swap them
            l += 1
            r -= 1
            # Now this segment is in increasing order, which is smallest possible permutation
