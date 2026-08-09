class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1, count2 = [0] * 26, [0] * 26
        # Populate counts for first window of len s1 in s2
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        # Count initial matches
        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
        
        # Use a sliding window of fixed len (len of s1)
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Right edge entering
            index = ord(s2[r]) - ord('a')
            count2[index] += 1
            if count1[index] == count2[index]:
                matches += 1
            elif count1[index] + 1 == count2[index]:
                matches -= 1
            
            # Left edge leaving
            index = ord(s2[l]) - ord('a')
            count2[index] -= 1
            if count1[index] == count2[index]:
                matches += 1
            elif count1[index] - 1 == count2[index]:
                matches -= 1
            
            l += 1
            
        return matches == 26

