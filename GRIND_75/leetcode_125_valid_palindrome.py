# Trivial Solution
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_str = ""

        for st in s:
            if st.isalnum():
                new_str += st.lower()

        return new_str == new_str[::-1]


# Optimal Solution
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1

        while (left < right):

            while (left < right and not self.alphanumcheck(s[left])):
                left += 1

            while (left < right and not self.alphanumcheck(s[right])):
                right -= 1

            if self.lower(s[left]) != self.lower(s[right]):
                return False

            left += 1
            right -= 1
        return True

    def alphanumcheck(self, s):
        return ('a' <= s <= 'z' or 'A' <= s <= 'Z' or '0' <= s <= '9')

    def lower(self, s):
        if 'A' <= s <= 'Z':
            return chr(ord(s) + 32)
        else:
            return s


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
