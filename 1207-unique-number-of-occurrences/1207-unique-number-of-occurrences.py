from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts=Counter(arr).values()
        return len(counts)==len(set(counts))


# Our Traditional Method without built-in things
        # freq = {}

        # for num in arr:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1

        # counts = list(freq.values())
        # return len(counts) == len(set(counts))