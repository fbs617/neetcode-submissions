import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        out = 0
        possible_ks = []
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            curr_t = 0
            for pile in piles:
                curr_t += math.ceil(pile / mid)
                if curr_t > h:
                    break
            if curr_t <= h:
                out = mid
                right = mid - 1
            else:
                left = mid + 1
        return out
        