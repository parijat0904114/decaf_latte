# Trivial Solution


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1

        majority_count = len(nums)//2
        for n in map:
            if map[n] > majority_count:
                return n


# Optimal Solution(Boyer Moore's Algorithm)


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        num = 0

        for n in nums:
            if count == 0:
                num = n
            count += 1 if n == num else -1
        return num


s = Solution()
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([6, 6, 6, 7, 7]))
