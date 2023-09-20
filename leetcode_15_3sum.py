class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        result = []

        for i in range(len(nums) - 2):
            a = nums[i]

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                b, c = nums[j], nums[k]
                triplet_sum = a + b + c
                if triplet_sum == 0:
                    result.append([a, b, c])
                    while (
                        j < k and nums[j] == nums[j + 1]
                    ):  # the loop is actually doing the trick moving b forward
                        j += 1
                    while (
                        j < k and nums[k] == nums[k - 1]
                    ):  # the loop is actually moving c backward
                        k -= 1
                    j += 1
                    k -= 1
                elif triplet_sum < 0:
                    j += 1
                else:
                    k -= 1
        return result


obj = Solution()
print(obj.threeSum([-1, 0, 1, 2, -1, -4]))
