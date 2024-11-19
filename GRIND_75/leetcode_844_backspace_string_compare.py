# Trivial Solution
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_1 = []
        stack_2 = []

        def string_formatter(st, stack):
            for s in st:
                if 'a' <= s <= 'z':
                    stack.append(s)
                elif stack:
                    stack.pop()
            return stack
        return string_formatter(s, stack_1) == string_formatter(t, stack_2)

# Optimized Solution (# TODO)


class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """


s = Solution()
print(s.backspaceCompare("ab#c", "ad#c"))
