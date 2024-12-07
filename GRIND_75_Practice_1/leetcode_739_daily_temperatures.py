# Monotonic Stack
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0]*len(temperatures)
        st = []

        for pos, temp in enumerate(temperatures):
            while st and temp > st[-1][0]:
                top = st.pop()
                res[top[1]] = pos - top[1]
            st.append([temp, pos])
        return res


s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
