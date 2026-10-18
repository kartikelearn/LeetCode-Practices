class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def solution(open_count, close_count, current):
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                solution(open_count + 1, close_count, current + "(")

            if close_count < open_count:
                solution(open_count, close_count + 1, current + ")")

        solution(0, 0, "")
        return result