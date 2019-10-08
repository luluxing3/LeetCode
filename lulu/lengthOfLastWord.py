class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for x in s.strip():
            if x != ' ':
                count += 1
            else:
                count = 0
        return count
