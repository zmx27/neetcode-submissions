class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand) # Use a counter to quickly build frequency map
        unique_keys = sorted(count.keys())
        for num in unique_keys:
            if count[num] > 0:
                needed_groups = count[num] # number of groups that needs num as the start
                for i in range(num, num+groupSize):
                    if count[i] < needed_groups:
                        return False # not enough numbers to add to all of the sequences
                    count[i] -= needed_groups
                
        return True

        
