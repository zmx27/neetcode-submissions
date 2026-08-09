class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l, r = 0, 0
        
        while r < len(nums):
            while q and nums[r] >= nums[q[-1]]:
                # Remove indices whose values are smaller than the new value
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r+1 >= k:
                # Reached size k
                # Front of deque represents the max
                res.append(nums[q[0]])
                l += 1
            
            r += 1
        
        return res
            
