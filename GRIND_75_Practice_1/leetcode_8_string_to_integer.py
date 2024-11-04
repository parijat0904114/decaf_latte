class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip(' ')
        sign = 1
        sign_map = {'+': 1, '-': -1}
        min_val = -2**31
        max_val = 2**31 - 1
        num = 0
        for i in range(0, len(s)):
            if i == 0 and s[i] in sign_map:
                sign = sign_map[s[0]]
            elif s[i] >= '0' and s[i] <= '9':
                num = int(s[i]) + num*10
                if sign*num < min_val:
                    return min_val
                elif sign*num > max_val:
                    return max_val
            else:
                return sign*num
        return sign*num


s = Solution()
print(s.myAtoi(" -042"))
print(s.myAtoi("1337c0d3"))
print(s.myAtoi("0-1"))
print(s.myAtoi("words and 987"))
print(s.myAtoi("-91283472332"))
