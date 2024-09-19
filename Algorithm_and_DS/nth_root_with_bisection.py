class Solution(object):
    def squareRoot(self, num, n):
        if 1<=n<=5:
            low = 0.0
            high = num
            while high - low > 0.00001:
                mid = low + (high - low)/2
                print('mid', mid)
                if mid**n > num:
                    high = mid 
                elif mid**n < num:
                    low = mid
                else:
                    return round(mid, 5)
            return round(mid, 5)
        return 'Please enter a number between 1 and 5'
s = Solution()
print(s.squareRoot(17, 9))
