class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqArr = [[] for _ in range(len(nums)+1) ]
        count = Counter(nums)
        for num, cnt in count.items():
            freqArr[cnt].append(num)
        
        res = []
        for i in range(len(freqArr)-1, -1, -1):
            for j in range(len(freqArr[i])):
                res.append(freqArr[i][j])
                if len(res) == k:
                    return res