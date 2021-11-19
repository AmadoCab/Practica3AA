class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = dict()

        def perm(ans,nums,combination,start,visited):
            n = len(nums)
            if len(combination) == n:
                ans.append(combination.copy())
                return None
            for i in range(n):
                if visited.get(nums[i]):
                    continue
                visited[nums[i]] = True
                combination.append(nums[i])
                perm(ans,nums,combination,i+1,visited)
                combination.pop()
                visited[nums[i]] = False

        perm(ans,nums,[],0,visited)
        return ans

# EOF #
