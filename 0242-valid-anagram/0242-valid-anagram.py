from collections import defaultdict
# from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s)==Counter(t)
        v_ans=defaultdict(int)
        for el in s:
            v_ans[el]+=1
        # v_ans=Counter(s) we can also use this.. instead
        for el in t:
            v_ans[el]-=1
        return all(values==0 for values in v_ans.values())