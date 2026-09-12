class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        sett=set()
        longest=0
        n=len(s)
        for start in range(n):
            while s[start] in sett:
                sett.remove(s[l])
                l+=1
            w=(start-l)+1
            longest=max(longest,w)
            sett.add(s[start])
        return longest