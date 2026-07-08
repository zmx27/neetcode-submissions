class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        # Timestamps sorted in ascending order because they're guaranteed to be increasing for each key
        self.store[key].append([value, timestamp])
        # key: list of [val, timestamp]
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1
        # Binary search to find the rightmost timestamp t <= timestamp
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                # Found a working value, record it
                # Look right to find larger timestamp if possible
                l = m + 1
                res = values[m][0]
            else:
                # Timestamp too large, look left
                r = m - 1

        return res
        
