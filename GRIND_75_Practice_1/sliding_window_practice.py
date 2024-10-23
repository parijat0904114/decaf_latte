class Solution(object):
    def sliding_window(self, str):
        left = 0
        start = 0
        output = 0
        seen = {}
        for right, ch in enumerate(str):
            if ch in seen:
                left = max(left, seen[ch] + 1)
            if right - left + 1 > output:
                output = right - left + 1
                start = left
            seen[ch] = right
        print(output, str[start:start+output])


s = Solution()
s.sliding_window('abcdaefghi')
