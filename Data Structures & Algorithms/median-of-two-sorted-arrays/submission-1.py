class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        i, j = 0, 0
        # Median1 is most recently picked, median2 is second most recently picked
        median1, median2 = 0, 0
        # Stop when half of the total number + 1 elements has been processed
        for k in range((len1+len2)//2 + 1):
            median2 = median1
            if i < len1 and j < len2:
                if nums1[i] < nums2[j]:
                    median1 = nums1[i]
                    i += 1
                else:
                    median1 = nums2[j]
                    j += 1
            elif i < len1:
                median1 = nums1[i]
                i += 1
            else:
                median1 = nums2[j]
                j += 1
        
        if (len1 + len2) % 2 == 0:
            return (median1 + median2) / 2
        else:
            return median1
            