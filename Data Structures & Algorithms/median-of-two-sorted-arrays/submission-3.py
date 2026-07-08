class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # Want to run binary search on A, which is the smaller array
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True: # We know there's a guaranteed median so we return when we find it
            i = (l+r) // 2 # pointer for A, represents index of last element in left partition
            j = half - i - 2 # pointer for B, extra subtract by 2 bc both indices start at 0

            # Any of the below can be out of bounds
            # Give default of -inf on the left and inf on the right
            # Deal with edge cases
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i+1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j+1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                # odd elements
                if total % 2 == 1:
                    return min(Aright, Bright) # cant have both be inf
                else: # even elements
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: # took too many elements from A
                r = i - 1
            else: # took too little elements from A
                l = i + 1