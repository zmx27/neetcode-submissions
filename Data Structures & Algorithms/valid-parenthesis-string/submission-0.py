class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == "*":
                star.append(i)
            else: # the char is a )
                if not left and not star:
                    return False
                if left: # pop from left stack first
                    left.pop()
                else: # then try the star stack
                    star.pop()
        
        while left and star:
            leftIndex, starIndex = left.pop(), star.pop()
            if leftIndex > starIndex:
                return False
        return not left