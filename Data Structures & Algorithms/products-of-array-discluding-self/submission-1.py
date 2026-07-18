class Solution:
    
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # output[i] will first store the product
        # of all numbers to the left of i
        output = [1] * n

        left_product = 1

        # Calculate left-side products
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]

        right_product = 1

        # Multiply by right-side products
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output


    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     prefix = [1]
    #     suffix = [0] * (len(nums) - 1)
    #     out = []
    #     suffix.append(1)
    #     for i in range(1, len(nums)):
    #         curr = nums[i-1] * prefix[i-1]
    #         prefix.append(curr)
    #     for i in range(len(nums) - 2, -1, -1):
    #         suffix[i] = suffix[i+1] * nums[i+1]
    #     for i in range(len(nums)):
    #         curr = prefix[i] * suffix[i]
    #         out.append(curr)
    #     return out

            