# Problem Link: https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checkerMap = {')': '(', '}': '{', ']': '['}

        if s[0] == ']' or s[0] == '}' or s[0] == ')':
            return False
        else:
            for c in s:
                if c in checkerMap:
                    if stack and stack[-1] == checkerMap[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)
            if not stack:
                return True
            else:
                return False