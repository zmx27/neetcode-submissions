class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Monotonically decreasing queue
        q = deque() # Tracks indices of elements
        # From left to right, the values the indices represent are in decreasng order
        output = []
        l, r = 0, 0 # l is beginning of the window
        while r < len(nums):
            while q and nums[r] >= nums[q[-1]]:
                # if curr element is already larger than prev added values, just remove them
                # they can't be a future max (reduces work)
                # smaller values will not be considered again
                q.pop()
            q.append(r) # Curr element added behind element strictly greater than it

            if l > q[0]: # Window advanced beyond oldest, can't use it anymore
                q.popleft()
                # Only pop once because only oldest element is stale and can't be considered

            if (r+1) >= k: # the window we are considering has reached size k
                output.append(nums[q[0]])
                l += 1 # left pointer incremented only when window is size k
            r += 1 # right pointer always advances
        return output    
