class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = {}
        for s in strs:
            curr_freq = [0] * 26
            for c in s:
                curr_freq[ord(c)-ord("a")] += 1
            curr_freq = tuple(curr_freq)
            if curr_freq in freqs:
                freqs[curr_freq].append(s)
            else:
                freqs[curr_freq] = [s]
        return list(freqs.values())


    
    # def isAnagram(self, s: str, t: str) -> bool:
    #     hs = {}
    #     ht = {}

    #     for c in s:
    #         if c in hs:
    #             hs[c] += 1
    #         else:
    #             hs[c] = 1
        
    #     for c in t:
    #         if c in ht:
    #             ht[c] += 1
    #         else:
    #             ht[c] = 1
        
    #     if ht == hs:
    #         return True
    #     return False