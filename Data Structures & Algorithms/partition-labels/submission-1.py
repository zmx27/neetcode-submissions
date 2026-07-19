class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        currSize = 0
        end = 0
        for i, c in enumerate(s):
            currSize += 1
            end = max(end, lastIndex[c])

            if i == end:
                res.append(currSize)
                currSize = 0
        return res
