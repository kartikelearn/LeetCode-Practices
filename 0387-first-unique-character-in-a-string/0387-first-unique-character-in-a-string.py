from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq=defaultdict(int)
        for el in s:
            freq[el]+=1
        for idx, ch in enumerate(s):
            if freq[ch] == 1:
                return idx
        return -1

