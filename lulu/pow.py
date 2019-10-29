class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1.0 / self.myPow(x, -n)

        dividePow = self.myPow(x, n/2)
        if n % 2 == 0:
            return dividePow * dividePow
        else:
            return dividePow * dividePow * x
