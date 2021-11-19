class Solution:
    def first(self,nums,target):
        l, r = 0, len(nums) - 1
        start = -1
        while l <= r:
            m = (r + l) // 2
            if target == nums[m]:
                start = m
                r = m - 1
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return start

    def last(self,nums,target):
        l, r = 0, len(nums) - 1
        end = -1
        while l <= r:
            m = (r + l) // 2
            if target == nums[m]:
                end = m
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return end

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.first(nums,target), self.last(nums,target)]

# EOF #
