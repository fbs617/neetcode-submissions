class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sequences = {}
        nums = set(nums)
        n_longest = 0
        for n in nums:
            # if (n+1) in sequences:
            #     curr_len = sequences[n+1] + 1
            #     n_longest = max(n_longest, curr_len)
            #     sequences[n] = curr_len
            #     continue
            curr_len = 1
            i = n
            while (i+1) in nums:
                curr_len += 1
                i += 1
            sequences[n] = curr_len
            n_longest = max(n_longest, curr_len)
        sequences = sequences.values()
        print(sequences)
        return max(sequences)
            