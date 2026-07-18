class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = {}
        ht = {}

        for c in s:
            if c in hs:
                hs[c] += 1
            else:
                hs[c] = 1
        
        for c in t:
            if c in ht:
                ht[c] += 1
            else:
                ht[c] = 1
        
        if ht == hs:
            return True
        return False







        
        # ls = list(s)
        # lt = list(t)
        # ls.sort()
        # lt.sort()
        # print(ls)
        # print(lt)
        # if ls == lt:
        #     return True
        # return False