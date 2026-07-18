class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [0] * (len(nums) - 1)
        out = []
        suffix.append(1)
        for i in range(1, len(nums)):
            curr = nums[i-1] * prefix[i-1]
            prefix.append(curr)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(len(nums)):
            curr = prefix[i] * suffix[i]
            out.append(curr)
        return out

            