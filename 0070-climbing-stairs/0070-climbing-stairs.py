from functools import cache
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        return self.climbStairs(n-1)+self.climbStairs(n-2)
        # memo = {}
        # def climb(n):
        #     if n <= 2:
        #         return n
        #     if n in memo:
        #         return memo[n]
        #     memo[n] = climb(n-1) + climb(n-2)
        #     return memo[n]
        # return climb(n)