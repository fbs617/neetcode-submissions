class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        s = s.lower().strip()
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and j > i:
                j -= 1
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
        