class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        # The int() casting is done solely to support
        # The division between two integers always truncates toward zero.

        op_map = {'+': lambda x, y: int(x + y),
                  '-': lambda x, y: int(x - y),
                  '*': lambda x, y: int(x * y),
                  '/': lambda x, y: int(x / y)
                  }

        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if token in op_map:
                b = float(st.pop())
                a = float(st.pop())
                st.append(op_map[token](a, b))
            else:
                st.append(token)
        return st.pop()
s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))