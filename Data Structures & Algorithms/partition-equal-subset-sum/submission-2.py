class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: # if odd sum, can't have two equal partitions
            return False
        
        target = total//2
        sums = set() # maintain a set of possible subset sums using the processed numbers
        sums.add(0) # guaranteed to have a sum of 0
        for i in range(len(nums)-1, -1, -1): # iterate in reverse order
            nextSums = set() # can't add to set while iterating through it so create a new set
            for t in sums:
                currSum = nums[i] + t
                if currSum == target: # stop early if found
                    return True
                nextSums.add(t) # don't want to lose original values, can also be skip current num
                nextSums.add(currSum) # take current number
            sums = nextSums # update the possible subset sums
        return True if target in sums else False