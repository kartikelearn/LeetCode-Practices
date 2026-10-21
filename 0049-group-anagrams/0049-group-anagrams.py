from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups=defaultdict(list)
        result=[]
        for el in strs:
            sorted_str=tuple(sorted(el))
            groups[sorted_str].append(el)
        for value in groups.values():
            result.append(value)
        return result


        