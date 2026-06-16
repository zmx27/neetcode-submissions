class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        freq_arr = [[] for i in range(len(nums) + 1)]
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        for num, count in freq.items():
            freq_arr[count].append(num)
        res = []
        for i in range(len(freq_arr)-1, 0, -1):
            for j in freq_arr[i]:
                res.append(j)
                if len(res) == k:
                    return res
