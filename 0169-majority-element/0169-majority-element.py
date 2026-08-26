class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for el in nums:
            freq[el]=freq.get(el,0)+1
        for key, val in freq.items():
            if val>(len(nums)//2):
                return key