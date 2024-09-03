class Solution(object):
    def postfix_to_prefix(self, tokens):
        st = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token in operators:
                b = st.pop()
                a = st.pop()
                st.append(token+a+b)
            else:
                st.append(token)
        return st
            
s = Solution()
print(s.postfix_to_prefix("abc/-ad/e-*"))