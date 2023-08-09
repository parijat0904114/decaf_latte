class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = "".join(x.lower() for x in s if x.isalnum())
        left_counter, right_counter = 0, len(s) - 1
        while left_counter < right_counter:
            if s[left_counter] != s[right_counter]:
                return False
            left_counter += 1
            right_counter -= 1
        return True
