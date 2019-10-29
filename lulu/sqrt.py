class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        left = 1
        right = x / 2
        last_mid = None
        while left <= right:
            mid = int((left + right) / 2)
            if x / mid > mid:
                left = mid + 1
                last_mid = mid
            elif x / mid < mid:
                right = mid - 1
            else:
                return mid
        return last_mid
