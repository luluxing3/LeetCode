class Solution(object):
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root and root.left is None and root.right is None:
            return root.val == sum
        if root:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        #if root:
        #    return self.hasPathSumRecursive(root.left, n - root.val) or self.hasPathSumRecursive(root.right, n - root.val)
        #else:
        #    return n == 0
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        result = self.pathSumRecursive(root)
        print(result)
        return sum in result

    def pathSumRecursive(self, root):
        if root is None:
            return []
        if root and root.left is None and root.right is None:
            return [root.val]
        result = []
        if root:
            for left_sum in self.pathSumRecursive(root.left):
                result.append(root.val + left_sum)
            for right_sum in self.pathSumRecursive(root.right):
                result.append(root.val + right_sum)
        return result

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        result = self.pathSumIterative(root)
        print(result)
        return sum in result
    
    def pathSumIterative(self, root):
        result = []
        aStack = []
        if root:
            aStack.append([root, 0])

        while aStack:
            nextStack = []
            for (p, n) in aStack:
                if p.left:
                    nextStack.append([p.left, n + p.val])
                if p.right:
                    nextStack.append([p.right, n + p.val])
                if p.left is None and p.right is None:
                    result.append(n + p.val)
            aStack = nextStack
        return result
            
            

            
