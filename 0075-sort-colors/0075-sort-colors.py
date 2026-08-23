class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        balls=[0]*3
        for colors in nums:
            balls[colors]+=1
        r,w,b=balls
        nums[:r]=r*[0]
        nums[r:r+w]=w*[1]
        nums[r+w:]=b*[2]

            
        