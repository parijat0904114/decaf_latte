# Brute Force Solution


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
            res = max(res, len(seen))
        return res

# Optimal Sliding Window Solution


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        sub_len = 0
        seen = dict()

        for i in range(len(s)):
            if s[i] in seen:
                l = max(seen[s[i]] + 1, l)
            seen[s[i]] = i
            sub_len = max(sub_len, i - l + 1)
        return sub_len


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
