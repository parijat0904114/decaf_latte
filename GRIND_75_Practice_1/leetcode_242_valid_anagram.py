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
            if st in counter:
                counter[st] += 1
            else:
                counter[st] = 1

        for st in t:
            if st not in counter:
                return False
            counter[st] -= 1
            if counter[st] < 0:
                return False
        return True

# s = Solution()
# print(s.isAnagram("anagram", "nagaram"))
# print(s.isAnagram("rat", "car"))

        