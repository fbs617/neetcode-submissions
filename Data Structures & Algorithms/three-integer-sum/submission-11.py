class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        for i in range(len(nums)):
            n = nums[i]
            if i > 0 and nums[i-1] == nums[i]:
                continue
            start = i + 1
            end = len(nums) - 1
            while start < end:
                s = nums[start]
                e = nums[end]
                if s + e + n == 0:
                    out.append([s,e,n])
                    end -= 1
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                if s + e + n > 0:
                    end -= 1
                elif s + e + n < 0:
                    start += 1
        return out