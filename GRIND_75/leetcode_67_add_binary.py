class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = self.rev(a)
        b = self.rev(b)
        res = ""
        carry = 0

        for i in range(max(len(a), len(b))):
            digit_a = ord(a[i]) - ord('0') if i < len(a) else 0
            digit_b = ord(b[i]) - ord('0') if i < len(b) else 0
            sum = digit_a + digit_b + carry
            res = str(sum % 2) + res
            carry = sum//2
        return res if not carry else str(carry) + res

    def rev(self, s):
        m = ""
        for st in s:
            m = st + m
        return m


s = Solution()
print(s.addBinary("1010", "1011"))
