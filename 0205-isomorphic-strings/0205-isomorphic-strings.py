class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = {}
        used = set()

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # If char_s already has a mapping
            if char_s in mapping:
                if mapping[char_s] != char_t:
                    return False

            # If char_s is new
            else:
                # char_t is already mapped from another character
                if char_t in used:
                    return False

                mapping[char_s] = char_t
                used.add(char_t)

        return True