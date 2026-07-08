class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1
        ans = -1

        while lower <= upper:
            time = 0
            k = (lower + upper) // 2
            for num in piles:
                time += math.ceil(num / k)
            if time <= h:
                ans = k
                upper = k - 1
            else:
                lower = k + 1
            
        return ans