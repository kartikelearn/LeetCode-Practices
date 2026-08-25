from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums)!=len(set(nums))
        # freq=Counter(nums)
        # return any(value>1 for value in freq.values())
        nums_set=set()
        for el in nums:
            if el in nums_set:
                return True
            nums_set.add(el)
        return False
            