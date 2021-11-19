class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = {
            4:True, 16:True, 37:True, 58:True, 89:True, 145:True, 42:True, 20:True
        }
        def get_next(number):
            total = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total += digit ** 2
            return total

        while n != 1 and not cycle.get(n,False):
            n = get_next(n)

        return n == 1

# EOF #
