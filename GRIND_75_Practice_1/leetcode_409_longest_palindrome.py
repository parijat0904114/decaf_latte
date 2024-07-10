class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}
        for st in s:
            if st not in counter:
                counter[st] = 1
            else:
                counter[st] += 1
        sum = 0
        carry = 0
        for c in counter:
            value = counter[c]//2
            sum += 2*value
            if not carry and counter[c]%2:
                carry = 1

        return sum + carry

# s = Solution()
# print(s.longestPalindrome('abccccdd'))
# print(s.longestPalindrome('ccc'))