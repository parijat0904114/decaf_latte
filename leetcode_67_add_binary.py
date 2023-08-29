class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        if len(a) == 1 and a[0] == "0":
            return b
        elif len(b) == 1 and b[0] == "0":
            return a

        if len(a) < len(b):
            while len(a) < len(b):
                a = "0" + a
        elif len(b) < len(a):
            while len(b) < len(a):
                b = "0" + b

        carry = 0
        sum = ""
        for i in range(len(a)):
            temp_sum = (int(a[len(a) - i - 1]) + int(b[len(b) - i - 1]) + carry) % 2
            carry = (int(a[len(a) - i - 1]) + int(b[len(b) - i - 1]) + carry) // 2
            sum = sum + str(temp_sum)
        if carry == 1:
            sum = sum + "1"
        return sum[::-1]


# obj = Solution()
# print(obj.addBinary("1000", "111111"))
