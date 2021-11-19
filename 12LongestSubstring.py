class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        else:
            maxl = 1
            slow, fast = 0, 1
            while fast < n:
                if s[fast] in s[slow:fast]:
                    slow += 1
                else:
                    fast += 1
                    if fast-slow > maxl:
                        maxl = fast-slow
        return maxl

# EOF #
