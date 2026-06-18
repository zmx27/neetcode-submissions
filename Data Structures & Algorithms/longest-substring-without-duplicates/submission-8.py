class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet: # Remove duplicates wherever it is
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r]) # Expand window and compare to curr max
            res = max(res, len(charSet))

        return res