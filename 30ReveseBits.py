class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            if (n | (1<<i)) == n:
                ans += 1 << (31-i)
        return ans

# EOF #
