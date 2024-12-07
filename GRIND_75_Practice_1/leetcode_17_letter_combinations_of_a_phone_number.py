class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        int_st_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                      "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if not digits:
            return []

        output = [""]

        for d in digits:
            temp = []
            for s in output:
                for c in int_st_map[d]:
                    temp.append(s+c)
            output = temp
        return output


s = Solution()
s.letterCombinations("23")
