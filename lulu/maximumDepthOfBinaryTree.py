class Solution(object):
    def maxDepthRecursive(self, root):
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0

    def maxDepthIterative(self, root):
        aStack = []
        if root:
            aStack.append(root)
        
        depth = 0
        while aStack:
            depth += 1
            nextStack = []
            for p in aStack:
                if p.left:
                    nextStack.append(p.left)
                if p.right:
                    nextStack.append(p.right)
            aStack = nextStack
        return depth
                
            
