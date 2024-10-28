class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_1 = []
        stack_2 = []

        def string_formatter(stri, stack):
            for st in stri:
                if st == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(st)
        string_formatter(s, stack_1)
        string_formatter(t, stack_2)

        return stack_1 == stack_2


s = Solution()
print(s.backspaceCompare("y#fo##f", "y#f#o##f"))
