class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: 
            return ""
        # Follows [length]#[string]...
        res = []
        for st in strs: 
            res.append(str(len(st)))
            res.append("#")
            res.append(st)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: 
            return []
        # Scans number by finding # delimiter, gets string by slicing
        res = []
        i = 0
        while (i < len(s)):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res
