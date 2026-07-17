class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand) # Use a counter to quickly build frequency map
        unique_keys = sorted(count.keys())
        for num in unique_keys: # iterates through unique keys in sorted order
            # minimum numbers are processed first
            if count[num] > 0:
                # this only triggers when num hasn't been completely processed already
                needed_groups = count[num] # number of groups that needs num as the start
                for i in range(num, num+groupSize):
                    if count[i] < needed_groups:
                        return False # not enough numbers to satisfy sequences required by num
                    count[i] -= needed_groups # batch subtraction

        return True # loop never returned false so return true

        
