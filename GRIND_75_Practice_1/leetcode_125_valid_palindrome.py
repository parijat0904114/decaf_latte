class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # using two pointer method for improved space complexity.

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while left < right and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def alphaNum(self, c):
        return (
            'a' <= c <= 'z' or
            'A' <= c <= 'Z' or
            '0' <= c <= '9'
        )


x = Solution()
print(x.isPalindrome("A man, a plan, a canal: Panama"))
print(x.isPalindrome(" "))
