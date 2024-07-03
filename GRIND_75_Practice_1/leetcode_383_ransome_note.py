class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counter = [0]*26
        for ch in magazine:
            counter[ord(ch) - 97] += 1
        for ch in ransomNote:
            counter[ord(ch) - 97] -= 1
        for cnt in counter:
            if cnt <0:
                return False
        return True

s = Solution()
print(s.canConstruct("aa", "aab"))