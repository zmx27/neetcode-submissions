class MinStack:

    def __init__(self):
        self.values = []
        self.minVals = []

    def push(self, val: int) -> None:
        if len(self.values) == 0:
            self.values.append(val)
            self.minVals.append(val)
        else:
            minVal = min(self.minVals[-1], val)
            self.values.append(val)
            self.minVals.append(minVal)
        

    def pop(self) -> None:
        if not self.values:
            return

        self.values.pop()
        self.minVals.pop()
        

    def top(self) -> int:
        if not self.values:
            return None
        return self.values[-1]
        

    def getMin(self) -> int:
        if not self.values:
            return None
        return self.minVals[-1]
