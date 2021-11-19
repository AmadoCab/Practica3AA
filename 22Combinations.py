class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def comb(n,k,start,combination,ans):
            if len(combination) == k:
                ans.append(combination.copy())
                return None
            for i in range(start, n+1):
                combination.append(i)
                comb(n,k,i+1,combination,ans)
                combination.pop()
        comb(n,k,1,[],ans)
        return ans

# EOF #
