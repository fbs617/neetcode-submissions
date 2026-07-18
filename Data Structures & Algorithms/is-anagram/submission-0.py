class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
        print(ls)
        print(lt)
        if ls == lt:
            return True
        return False