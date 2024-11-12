# Optimized Solution
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses_map = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for str in s:
            if str in parentheses_map:
                stack.append(parentheses_map[str])
            elif not stack or str != stack.pop():
                return False
        return not stack


s = Solution()
print(s.isValid("()[]{}"))
