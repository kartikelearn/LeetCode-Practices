class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # i=0
        # def power(i,n):
        #     if 2**i==n:
        #         return True
        #     elif 2**i>n:
        #         return False
        #     else:
        #         return power(i+1,n)
        # return power(i,n)
        def power(n):
            if n==1:
                return True
            elif n<1 or n%2!=0:
                return False
            else:
                return power(n//2)
        return power(n)
            
            