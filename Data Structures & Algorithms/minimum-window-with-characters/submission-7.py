class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""

        tMap = {}
        for i in range(len(t)):
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        
        have = 0
        need = len(tMap)
        l = 0
        bestRange = [-1, -1]
        minLength = float("inf")
        sMap = {}
        for r in range(len(s)):
            c = s[r]
            sMap[c] = sMap.get(c, 0) + 1

            if c in tMap and sMap[c] == tMap[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < minLength:
                    minLength = r-l+1
                    bestRange = [l, r]
                
                c = s[l]
                sMap[c] -= 1
                if c in tMap and sMap[c] < tMap[c]:
                    have -= 1
                l += 1
            
        l, r = bestRange
        return s[l:r+1] if minLength != float("inf") else ""
             
        
        