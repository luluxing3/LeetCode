class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        for i in range(len(s)):
            charSet = set(s[i])
            currLength = 1
            for j in range(i + 1, len(s)):
                if s[j] not in charSet:
                    charSet.add(s[j])
                    currLength += 1
                else:
                    maxLength = max(maxLength, currLength)
                    break
            maxLength = max(maxLength, currLength)
        return maxLength

                
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        subStr = ''
        i = 0
        while i < len(s):
            if s[i] not in subStr:
                subStr += s[i]
            else:
                maxLength = max(maxLength, len(subStr))
                startIndex = subStr.index(s[i]) + 1
                subStr = subStr[startIndex:] + s[i]
            i += 1
        maxLength = max(maxLength, len(subStr))
        return maxLength
