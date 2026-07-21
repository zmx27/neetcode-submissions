class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = []
        for s in strs:
            length = len(s)
            res.append(str(length) + "#" + s)
        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j+1
            res.append(s[i:i+length])
            i += length
        return res
