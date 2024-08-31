class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        left = 0
        # st = 0
        output = 0
        # Uncomment iff we want to see the sequence.
        for right, ch in enumerate(s):
            if ch in seen:
                left = max(left, seen[ch]+1)
            if right - left + 1 > output:
                output = right - left + 1
                # st = left
            seen[ch] = right
        return output
        # return output, s[st:st+output]
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbd"))
print(s.lengthOfLongestSubstring("pwwkew"))