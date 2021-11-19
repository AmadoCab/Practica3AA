class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        book = {val:0 for val in s1}
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        else:
            for i in range(n2-n1+1):
                if sorted(s1) == sorted(s2[i:i+n1]):
                    return True
            return False

# Mejorable #
