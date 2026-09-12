class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen=set()
        repeated=set()
        k=10
        for i in range(len(s)-k+1):
            window=s[i:i+k]
            if window in seen:
                repeated.add(window)
            else:
                seen.add(window)
        return list(repeated)
