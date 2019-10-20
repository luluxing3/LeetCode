class Solution(object):
    def combination(self, n, k):
        if k == 1:
            return [[x] for x in range(1, n + 1)]
        for x in range(1, n + 1):
            
