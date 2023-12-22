class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash1 = {}
        hash2 = {}
        for m in magazine:
            if m not in hash1:
                hash1[m] = 1
            else:
                hash1[m] += 1

        for r in ransomNote:
            if r not in hash2:
                hash2[r] = 1
            else:
                hash2[r] += 1

        print(hash1, hash2)
        for key in hash2:
            if key not in hash1:
                return False
            elif hash1[key] < hash2[key]:
                return False
        return True


# obj = Solution()
# print(obj.canConstruct("a", "b"))
# print(obj.canConstruct("aa", "aab"))
