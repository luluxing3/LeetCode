class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        aStack = []
        for x in path.strip().split('/'):
            if x == '..':
                if aStack:
                    aStack.pop()
            elif not x or x == '.':
                pass
            else:
                aStack.append(x)
        canical_path = '/'.join(aStack)
        return '/' + canical_path
