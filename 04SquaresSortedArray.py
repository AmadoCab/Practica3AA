class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        ans = [0] * len(nums)
        while left <= right:
            lval = nums[left]
            rval = nums[right]
            i = right-left
            if abs(lval) >= abs(rval):
                ans[i] = lval*lval
                left += 1
            else: # abs(lval) <= abs(rval):
                ans[i] = rval*rval
                right -= 1
        return ans

# EOF #
