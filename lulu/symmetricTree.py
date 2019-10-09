class Solution(object):
    def isSymmetric(self, root):
        if root:
            return self.helper(root.left, root.right)
        else:
            return True

    def helper(self, left, right):
        if left and right:
            return left.val == right.val and self.helper(left.left, right.right) and self.helper(left.right, right.left)
        else:
            return (left is None) and (right is None)

    def isSymmetric(self, root):
        reverse_root = self.reverse(root)
        return self.isSameTree(root, reverse_root)

    def reverse(self, root):
        if root:
            newNode = TreeNode(root.val)
            newNode.left = self.reverse(root.right)
            newNode.right = self.reverse(root.left)
            return newNode
        else:
            return None

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return q.val == p.val and self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
        else:
            return (p is None) and (q is None)
        
