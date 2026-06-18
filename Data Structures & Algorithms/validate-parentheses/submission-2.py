class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open_pairs = {"}": "{", ")": "(", "]": "["}

        for c in s:
            if c in close_open_pairs:
                if (len(stack) != 0 and stack[-1] == close_open_pairs[c]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
        