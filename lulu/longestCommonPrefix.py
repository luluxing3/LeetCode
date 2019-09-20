class Solution(object):
    def getLongPrefixPair(self, x, y):
        if not x or not y:
            return ''
        if x[0] == y[0]:
            return x[0] + self.getLongPrefixPair(x[1:], y[1:])
        else:
            return ''

    def getLongPrefix(self, strs):
        if not strs:
            return ''
        longestPrefix = strs[0]
        for string in strs[1:]:
            longestPrefix = self.getLongPrefixPair(longestPrefix, string)
        return longestPrefix
        


            
