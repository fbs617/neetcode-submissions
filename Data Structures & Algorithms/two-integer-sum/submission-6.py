class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nset = set(nums)
        for n in nums:
            m = target - n
            if m in nset:
                if (m == n and (m != len(nums) - 1)):
                    return [nums.index(n),nums.index(m, nums.index(m) + 1)]
                elif m != n:
                    return [nums.index(n),nums.index(m)]