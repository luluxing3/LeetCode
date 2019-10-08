class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenthes_map = {')': '(', ']': '[', '}': '{'}
        aStack = []
        for x in s:
            if x in parenthes_map:
                if aStack and aStack[-1] == parenthes_map[x]:
                    aStack.pop()
                else:
                    return False
            else:
                aStack.append(x)
        if aStack:
            return False
        else:
            return True
