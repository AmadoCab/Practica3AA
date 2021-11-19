class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def ParenthGen(open, closed):
            if open == closed == n:
                result.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                ParenthGen(open + 1, closed)
                stack.pop()

            if closed < open:
                stack.append(")")
                ParenthGen(open, closed + 1)
                stack.pop()

        ParenthGen(0,0)
        return result

# EOF #
