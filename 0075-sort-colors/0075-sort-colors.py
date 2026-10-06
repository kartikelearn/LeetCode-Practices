class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counts=[0]*3
        # for colors in nums:
        #     counts[colors]+=1
        # r,w,b=counts
        # nums[:r]=r*[0]
        # nums[r:r+w]=w*[1]
        # nums[r+w:]=b*[2]
        # Bubble Sort
        j=0
        while j<len(nums)-1:
            i=0
            while i<len(nums)-1-j:
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                i+=1
            j+=1
