#leetcode generateParentheses
class Solution:
    def generateParenthesis(self, n):
        output = []
        stack = [("", n, n)]
        while stack:
            paren, _open, _close = stack.pop()
            if _open == 0:
                paren += ")" * _close
                output.append(paren)
            elif _open == _close:
                stack.append((paren + "(", _open - 1, _close))
            else:
                stack.append((paren + "(", _open - 1, _close))
                stack.append((paren + ")", _open, _close - 1))
        return output