class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): # Not equal len means not valid
            return False
        count = [0] * 26 # One index for each possible alphabet
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 # Increment for s
            count[ord(t[i]) - ord('a')] -= 1 # Decrement for t
        for num in count:
            if num != 0: # If freq counts match, all are 0
                return False
        return True


        