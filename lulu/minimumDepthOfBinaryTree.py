class Solution(object):
    def minDepthRecursive(self, root):
        if root:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        else:
            return 0

    def minDepthStack(self, root):
        aSack = [root]
        depth = 0
        while aStack:
            nextStack = []
            for p in aSack:
                if p is None:
                    return depth
                else:
                    nextStack.append(p.left)
                    nextStack.append(p.right)
            depth += 1
            aStack = nextStack




