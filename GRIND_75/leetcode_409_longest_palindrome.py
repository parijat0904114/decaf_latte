class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = [0]*52

        for st in s:
            if 'A' <= st <= 'Z':
                counter[ord(st) - ord('A')] += 1
            else:
                counter[ord(st) - 71] += 1

        sum = 0
        carry = 0

        for count in counter:
            sum += 2*(count//2)
            if not carry and count % 2 == 1:
                carry = 1
        return sum + carry


s = Solution()
print(s.longestPalindrome("abccccdd"))
