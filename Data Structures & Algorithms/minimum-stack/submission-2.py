class MinStack:

    def __init__(self):
        self.minVal = float("inf")
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(0)
            self.minVal = val
        else:
            diff = val - self.minVal
            self.stack.append(diff)
            if diff < 0:
                self.minVal = val

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.minVal = self.minVal - pop


    def top(self) -> int:
        if not self.stack:
            return None
        
        top = self.stack[-1]
        if top > 0:
            return top + self.minVal
        else:
            return self.minVal
        

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.minVal
        
