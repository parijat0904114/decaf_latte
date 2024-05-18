import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left_counter, right_counter = 0, len(s) - 1
        while left_counter < right_counter:
            if s[left_counter] != s[right_counter]:
                return False
            left_counter += 1
            right_counter -= 1
        return True

# s = Solution()
# print(s.isPalindrome("A man, a plan, a canal: Panama"))