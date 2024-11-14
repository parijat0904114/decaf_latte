class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counter = [0]*26
        for m in magazine:
            counter[ord(m) - ord('a')] += 1
        for r in ransomNote:
            if counter[ord(r) - ord('a')] == 0:
                return False
            counter[ord(r) - ord('a')] -= 1
        return True
