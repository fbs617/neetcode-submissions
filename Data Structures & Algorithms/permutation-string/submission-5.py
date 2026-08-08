class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       if len(s1) > len(s2):
            return False
       s1 = sorted(s1)
       i = 0
       j = len(s1) - i
       for k in range(j, len(s2)+1):
        sub_s2 = s2[i:k]
        sub_s2 = sorted(sub_s2)
        if sub_s2 == s1:
            return True
        i += 1
        
       return False
    
 