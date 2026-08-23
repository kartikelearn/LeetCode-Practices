import collections as defauldict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r_dic=defaultdict(list)
        result=[]
        for s in strs:
            sorted_s=tuple(sorted(s))
            r_dic[sorted_s].append(s)
        for values in r_dic.values():
            result.append(values)
        return result