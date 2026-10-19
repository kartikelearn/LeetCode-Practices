from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return Counter(s)==Counter(t)
        ans=defaultdict(int)
        for el in s:
            ans[el]+=1
        # ans=Counter(s) we can also use this.. instead
        for el in t:
            ans[el]-=1
        return all(values==0 for values in ans.values())
        