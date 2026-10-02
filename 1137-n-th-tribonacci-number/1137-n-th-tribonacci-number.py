from functools import cache
class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def trib(n):
            if n<=1:
                return n
            elif n==2:
                return 1
            else:
                return trib(n-1)+trib(n-2)+trib(n-3)
        return trib(n)