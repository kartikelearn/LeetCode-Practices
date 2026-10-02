class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i=0
        def power(i,n):
            if 3**i==n:
                return True
            elif 3**i>n:
                return False
            else:
                return power(i+1,n)
        return power(i,n)