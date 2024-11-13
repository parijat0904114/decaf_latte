# Recursive Solution
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        def b_search(low, high):
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            if low <= high:
                if nums[mid] < target:
                    return b_search(mid + 1, high)
                else:
                    return b_search(low, mid - 1)
            return -1
        return b_search(low, high)

# Iterative Optimal Solution


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 9))
