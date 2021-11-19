class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        S = S.lower()
        n = len(S)
        ans = []
        def perm(i, res):
            if i < n:
                perm(i+1, res + S[i])
                if S[i].islower(): perm(i+1, res + S[i].upper())
            else:
                ans.append(res)
        perm(0,'')
        return ans

# EOF #
