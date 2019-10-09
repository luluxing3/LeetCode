class Solution(object):
    def __init__(self):
        self.depth = {}
    def isBalanced(self, root):
        if root:
            left_depth = self.deep(root.left)
            right_depth = self.deep(root.right)
            return abs(left_depth - right_depth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return True

    def deep(self, root):
        if root:
            if root in self.depth:
                ans = self.depth[root]
            else:
                ans = 1 + max(self.deep(root.left), self.deep(root.right))
                self.depth[root] = ans
            return ans
        else:
            return 0
