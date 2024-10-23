class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_int_map = {'I': 1, 'V': 5, 'X': 10,
                         'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        for r in range(len(s)):
            print(r)
            i += roman_int_map[s[r]]
            if r < len(s)-1:
                if s[r] == 'I' and s[r+1] in ['V', 'X']:
                    i -= 2
                elif s[r] == 'X' and s[r+1] in ['L', 'C']:
                    i -= 20
                elif s[r] == 'C' and s[r+1] in ['D', 'M']:
                    i -= 200

        return i


s = Solution()
print(s.romanToInt('III'))
