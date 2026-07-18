class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        robbed = False
        for i in range(len(nums)):
            if (i == 0):
                dp[0] = nums[i]
                continue
            elif (i == 1):
                dp[1] = max(nums[1], nums[0])
                continue
            rob = nums[i] + dp[i-2]
            skip = dp[i-1]
            dp[i] = max(rob,skip)
        l = len(nums)
        return dp[l-1]

            