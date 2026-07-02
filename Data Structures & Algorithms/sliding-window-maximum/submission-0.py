class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # Tracks indices of elements
        # For left to right, the values are in decreasng order
        output = []
        l, r = 0, 0
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if l > q[0]: # Window advanced beyond index of maximum, can't use it anymore
                q.popleft()

            if (r+1) >= k: # queue reached the size of window, window is size k
                output.append(nums[q[0]])
                l += 1 # left pointer incremented when window is size k
            r += 1 # right pointer always advances
        return output    
