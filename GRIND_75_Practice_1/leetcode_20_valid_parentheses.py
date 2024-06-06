class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses_map = {'(': ')', '{': '}', '[': ']'}
        tracker = []
        for p in s:
            if p in parentheses_map:
                tracker.append(parentheses_map[p])
            elif not tracker or p != tracker.pop():
                return False
        return not tracker

# s = Solution()
# print(s.isValid("()[]{}"))