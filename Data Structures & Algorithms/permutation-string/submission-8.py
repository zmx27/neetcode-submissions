class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        need = len(count1)
        have = 0
        currMap = {}
        maxLen = len(s1)
        l = 0
        for r in range(len(s2)):
            # Right edge entering window
            char_r = s2[r]
            currMap[char_r] = 1 + currMap.get(char_r, 0)
            if char_r in count1 and currMap[char_r] == count1[char_r]:
                have += 1
            
            # Decrease window length when it gets to maxLen
            if (r-l+1) > maxLen:
                char_l = s2[l]
                if char_l in count1 and currMap[char_l] == count1[char_l]:
                    have -= 1
                currMap[char_l] -= 1
                l += 1
            
            # Check if match
            if have == need:
                return True
        
        return False