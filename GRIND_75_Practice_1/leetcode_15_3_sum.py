class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        n = len(nums)
        res = []

        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue

            # using two pointer method
            left, right = i + 1, n - 1
            print(left, right)
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[left] == nums[left + 1]:
                        left+=1
                    while left<right and nums[right] == nums[right - 1]:
                        right-=1
                    left+=1
                    right-=1
        return res

s = Solution()
s.threeSum([0,0,0])