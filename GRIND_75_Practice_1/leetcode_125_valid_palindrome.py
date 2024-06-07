import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        length = len(s)
        for i in range(length//2):
            if s[i] != s[length - i - 1]:
                return False
        return True
        
        
# x = Solution()
# print(x.isPalindrome("A man, a plan, a canal: Panama"))
# print(x.isPalindrome(" "))