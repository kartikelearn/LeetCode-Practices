from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dictio=Counter(arr)
        l=[]
        s=set()
        for values in dictio.values():
            l.append(values)
            s.add(values)
        return len(l)==len(s)