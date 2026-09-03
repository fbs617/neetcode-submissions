class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # length = len(nums)
        # i = 0
        # j = 0
        # speed = 2
        # loops = 0
        # while True:
        #     if i != j and nums[i] == nums[j]:
        #         return nums[i]
        #     if loops % 2 == 0:
        #         speed += 1
        #     i += 1
        #     i %= length
        #     j += speed
        #     j %= length
        #     loops += 1

        i = nums[0]
        j = nums[0]
        while True:
            i = nums[i]
            j = nums[nums[j]]
            if i == j:
                break
        i = nums[0]
        while i != j:
            i = nums[i]
            j = nums[j]
        return i
        
        