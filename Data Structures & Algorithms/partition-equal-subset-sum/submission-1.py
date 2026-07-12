class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: # if odd sum, can't have two equal partitions
            return False
        
        target = total//2
        sums = set() # maintain a set of possible sums
        sums.add(0) # guaranteed to have a sum of 0
        for i in range(len(nums)-1, -1, -1): # iterate in reverse order
            nextSums = set() # can't add to set while iterating through it so create a new set
            for t in sums:
                if t == target:
                    return True
                currSum = nums[i] + t
                nextSums.add(t) # add the sum that was already present to not lose values
                nextSums.add(currSum)
            sums = nextSums
        return False