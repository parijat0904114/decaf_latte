# Trivial Solution with sorting
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

# Solution 2 (Supports Unicode)


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        counter = {}

        for st in s:
            if st not in counter:
                counter[st] = 1
            else:
                counter[st] += 1

        for st in t:
            if st not in counter:
                return False
            counter[st] -= 1
            if counter[st] < 0:
                return False

        return True

# Solution 3 (Precise but only ASCII supporting)


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        counter = [0] * 26

        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1

        for count in counter:
            if count != 0:
                return False
        return True


s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
