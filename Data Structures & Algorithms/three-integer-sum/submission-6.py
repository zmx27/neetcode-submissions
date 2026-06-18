class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:   
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if (a > 0): # Smallest element is positive, can't sum to 0
                break
            
            if i > 0 and nums[i - 1] == a: # Curr value is a duplicate
                continue
            
            left = i+1
            right = len(nums) - 1
            while (left < right):
                target = a * -1
                curr = nums[left] + nums[right]
                if (curr > target):
                    right -= 1
                elif (curr < target):
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return res


