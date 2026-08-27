class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A          # always binary search the smaller one

        m, n = len(A), len(B)
        half = (m + n + 1) // 2  

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2   # take i elements from A
            j = half - i         # take rest from B

            Aleft  = A[i-1] if i > 0 else float('-inf')
            Aright = A[i]   if i < m else float('inf')
            Bleft  = B[j-1] if j > 0 else float('-inf')
            Bright = B[j]   if j < n else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2:
                    return max(Aleft, Bleft)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                hi = i - 1       # took too much from A
            else:
                lo = i + 1       # took too little from A