class Solution:
    def countCommas(self, n: int) -> int:
        commas = 0
        length = len(str(n))
        for group in range(1, (length - 1) // 3 + 1):
            lower = 10 ** (group * 3)
            upper = min(n, 10 ** ((group + 1) * 3) - 1)
            count = upper - lower + 1
            if count > 0:
                commas += count * group
        return commas
