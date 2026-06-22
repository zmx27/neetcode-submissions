class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (t == "" or len(t) > len(s)):
            return ""
        
        sMap, tMap = {}, {}
        # Populate map with frequency count of each char in t
        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)
        
        resWindow, resLen = [-1, -1], float("inf")
        have = 0
        need = len(tMap)
        l = 0
        for r in range(len(s)):
            c = s[r]
            sMap[c] = 1 + sMap.get(c, 0)

            if c in tMap and sMap[c] == tMap[c]:
                have += 1
            
            # Need a loop to keep shrinking window if necessary
            while have == need: # Window is valid
                # Update our result
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    resWindow = [l, r]
                
                # Pop from left of window to shrink it
                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
        
        l, r = resWindow
        return s[l:r+1] if resLen != float("inf") else ""
                

                

