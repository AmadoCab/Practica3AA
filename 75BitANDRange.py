class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if len(bin(left)) != len(bin(right)):
            return 0
        ans = left
        for i in range(left+1,right+1):
            ans &= i
        return ans

# EOF #
