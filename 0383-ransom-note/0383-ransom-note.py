from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            ransomNote_freq=Counter(ransomNote)
            magazine_freq=Counter(magazine)
            return all(ransomNote_freq[c] <= magazine_freq[c] for c in ransomNote)

# Later Do it using Dict only...