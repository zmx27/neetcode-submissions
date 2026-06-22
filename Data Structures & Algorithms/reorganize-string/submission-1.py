class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)
        maxHeap = [(-cnt, c) for c, cnt in count.items()]
        heapq.heapify(maxHeap)

        res = ""
        prev = None # Just used and cannot be immediately reused
        while maxHeap or prev: 
            if not maxHeap and prev: # no more chars to pop but prev still exists means forced to put same chars adj
                return ""
            
            cnt, c = heapq.heappop(maxHeap)
            cnt += 1
            res += c
            # Push prev back into heap after curr char is processed
            if prev:
                heapq.heappush(maxHeap, prev)

            if cnt != 0:
                prev = (cnt, c)
            else:
                prev = None # No need to pass on prev if count of curr char is 0
        
        return res