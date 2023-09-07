class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_counter = {}
        for st in s:
            if st in word_counter:
                word_counter[st] += 1
            else:
                word_counter[st] = 1
        sum = 0
        for word in word_counter:
            sum += (word_counter[word] // 2) * 2

        return sum if sum == len(s) else sum + 1


# obj = Solution()
# print(obj.longestPalindrome("a"))
