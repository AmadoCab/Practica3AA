class Solution:
    def rob(self, nums: List[int]) -> int:
        def prob(nums):
            rob, noRob = 0, 0
            for n in nums:
                newRob = max(rob+n, noRob)
                rob, noRob = noRob, newRob
            return noRob

        return max(nums[0], prob(nums[1:]), prob(nums[:-1]))

# EOF #
