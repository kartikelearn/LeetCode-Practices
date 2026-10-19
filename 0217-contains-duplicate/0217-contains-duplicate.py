class Solution(object):
    def containsDuplicate(self, nums):
        # uniques=set()
        # for el in nums:
        #     if el in uniques:
        #         return True
        #     uniques.add(el)
        # return False
        return len(nums)!=len(set(nums))