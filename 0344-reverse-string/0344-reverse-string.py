class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        def reverse(left,s,right):
            if left>=right:
                return 
            s[left], s[right] = s[right], s[left]
            return reverse(left+1,s,right-1)
        reverse(left,s,right)