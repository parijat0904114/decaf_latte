class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses_map = {"(": ")", "{": "}", "[": "]"}
        st = []
        for p in s:
            if p in parentheses_map:
                st.append(parentheses_map[p])
            elif not st or p != st.pop():
                return False
        return not st


# s = Solution()
# print(s.isValid("()[]{}"))
# print(s.isValid("(]"))
