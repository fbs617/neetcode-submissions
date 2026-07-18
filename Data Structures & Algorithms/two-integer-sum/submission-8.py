class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        i = 0
        for n in nums:
            if (target - n) in prev:
                return [prev[target-n], i]
            prev[n] = nums.index(n)
            i += 1