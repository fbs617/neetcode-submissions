class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        pivot = lo

        def bsearch(start, end):
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1

        left = bsearch(0, pivot - 1)
        if left != -1:
            return left
        else:
            return bsearch(pivot, len(nums) - 1)