class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ri_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        num = 0
        length = len(s)
        for i in range(length):
            if i + 1 < length and ri_map[s[i+1]] > ri_map[s[i]]:
                num -= ri_map[s[i]]
            else:
                num += ri_map[s[i]]
        return num


s = Solution()
print(s.romanToInt('MCMXCIV'))
