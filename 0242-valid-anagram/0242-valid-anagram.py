from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        if len(t)!=len(s):
            return False
        set_s=set(s)
        for el in set_s:
            if s.count(el)!=t.count(el):
                return False
        return True

        