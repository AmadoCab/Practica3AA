class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = 0
        noRob = 0
        for i in range(len(nums)):
            newRob = noRob + nums[i]
            newNoRob = max(noRob, rob)
            rob, noRob = newRob, newNoRob
        return max(rob, noRob)

# EOF #
