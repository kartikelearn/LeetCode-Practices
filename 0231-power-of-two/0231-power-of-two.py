class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i=0
        def power(i,n):
            if 2**i==n:
                return True
            elif 2**i>n:
                return False
            else:
                return power(i+1,n)
        return power(i,n)
            
            