class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) == 1 and a[0] == '0':
            return b
        if len(b) == 1 and b[0] == '0':
            return a
        if len(a) < len(b):
            while len(a) < len(b):
                a = '0' + a
        else:
            while len(b) < len(a):
                b = '0' + b
        sum = ""
        carry = 0
        for i in reversed(range(len(a))):
            sum += str((int(a[i]) + int(b[i]) + carry)%2)
            carry = (int(a[i]) + int(b[i]) + carry)//2
        if carry:
            sum += '1'
        return sum[::-1]
# s = Solution()
# print(s.addBinary('1010', '1011'))
# print(s.addBinary('11', '1'))