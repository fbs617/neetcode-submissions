class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            s = numbers[start]
            e = numbers[end]
            if s + e == target:
                return[start+1,end+1]
            elif s + e > target:
                end -= 1
            else:
                start += 1
        