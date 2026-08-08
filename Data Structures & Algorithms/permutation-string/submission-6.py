from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0

        target = Counter(s1)

        for i in range(len(s1), len(s2) + 1):

            current_str = s2[left:i]

            if Counter(current_str) == target:
                return True

            left += 1

        return False










# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
    #    if len(s1) > len(s2):
    #         return False
    #    s1 = sorted(s1)
    #    i = 0
    #    j = len(s1) - i
    #    for k in range(j, len(s2)+1):
    #     sub_s2 = s2[i:k]
    #     sub_s2 = sorted(sub_s2)
    #     if sub_s2 == s1:
    #         return True
    #     i += 1
        
    #    return False
    
 