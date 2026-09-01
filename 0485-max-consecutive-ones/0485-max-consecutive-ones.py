class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans=[]
        for i in range(len(nums)):
            if nums[i]==0:
                count=0
                ans.append(count)
            else:
                count+=1
                ans.append(count)
        return max(ans)