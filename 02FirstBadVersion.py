# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            middle = (left+right)//2
            if not isBadVersion(middle):
                left = middle + 1
            else:
                right = middle
        return left

# EOF #
