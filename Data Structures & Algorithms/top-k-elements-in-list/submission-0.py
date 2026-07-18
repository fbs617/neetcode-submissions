class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {} # store each num with frequency
        out = []
        for num in nums:
            freq = num_freq.get(num, [num, 0])[1]
            num_freq[num] = [num, freq + 1]
        values = num_freq.values()
        values = sorted(values, key=lambda x:x[1], reverse=True)
        values = values[:k]
        for value in values:
            out.append(value[0])
        return out