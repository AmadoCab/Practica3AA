class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ans = [0] * n
        i = 0
        for num in nums:
            if num != 0:
                ans[i] = num
                i += 1
        print(ans)
        nums[:] = ans

# EOF #
